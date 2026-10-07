import pandas as pd
import os
from transformers import BertTokenizer, BertModel
import torch
import fitz  # PyMuPDF
import re
import numpy as np
from docx import Document

def read_pdf(file_path):
    """从PDF文件中提取所有文本内容"""
    text = ''
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def read_docx(file_path):
    """从Word文件中提取所有文本内容"""
    doc = Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

def process_resume(file_path):
    """处理简历文件，自动判断文件类型并提取文本"""
    if file_path.endswith('.pdf'):
        resume_text = read_pdf(file_path)
    elif file_path.endswith('.docx'):
        resume_text = read_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or Word document.")
    # 此处可以加入文本预处理逻辑
    cleaned_text = clean_text(resume_text)
    # 返回清洗后的文本
    return cleaned_text

def clean_text(text):
    """基本的文本清洗流程"""
    text = text.lower()  # 转换为小写
    text = re.sub(r"[^\w\s]", '', text)  # 移除标点
    text = re.sub(r"\s+", ' ', text)  # 合并多余空格
    return text.strip()

# 假设 process_resume 已经定义且可以处理PDF文件，返回文本内容
# 假设 get_embeddings 和 calculate_similarities 函数也已经定义

# 加载模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert')
model = BertModel.from_pretrained('bert')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def get_embeddings(texts, batch_size=32):
    """调整文本批处理大小，确保不超过模型限制，并适应设备内存"""
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        inputs = tokenizer(batch_texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        all_embeddings.extend(embeddings)
    return np.array(all_embeddings)

def calculate_similarities(embedding, embeddings):
    """计算向量与向量集合之间的余弦相似度"""
    if embedding.ndim > 1:
        embedding = embedding.squeeze()
    
    norms_embedding = np.linalg.norm(embedding)
    norms_embeddings = np.linalg.norm(embeddings)
    cos_sim = np.dot(embeddings, embedding) / (norms_embeddings * norms_embedding)
    return cos_sim


def load_job_data(file_path, job_id):
    """加载特定ID的工作岗位信息"""
    jobs_df = pd.read_csv(file_path)
    selected_job = jobs_df[jobs_df['id'] == job_id].iloc[0]
    job_info = ' '.join([str(selected_job[field]) for field in ['title', 'description', 'education', 'salary']])
    return job_info

def main():
    job_id = 0  # 假设我们选择ID为0的工作岗位
    job_description = load_job_data("data_all.csv", job_id)
    job_embedding = get_embeddings([job_description])

    resumes_folder = "resumes"
    candidates = []
    for resume_file in os.listdir(resumes_folder):
        if resume_file.endswith('.pdf'):
            resume_path = os.path.join(resumes_folder, resume_file)
            resume_text = process_resume(resume_path)
            resume_embedding = get_embeddings([resume_text])
            similarity = calculate_similarities(job_embedding, resume_embedding)
            candidates.append((resume_file, similarity))

    # 根据相似度排序，选择最匹配的候选人
    candidates.sort(key=lambda x: x[1], reverse=True)
    
    # 打印最匹配的几个候选人
    print("最匹配的候选人列表：")
    for candidate in candidates[:2]:  # 只展示前5个最匹配的
        print(f"{candidate[0]}: 相似度={candidate[1]}")

if __name__ == "__main__":
    main()
