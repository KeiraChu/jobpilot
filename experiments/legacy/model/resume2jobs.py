import fitz
import re
from docx import Document
import pytesseract
from PIL import Image
from transformers import BertTokenizer, BertModel
import torch
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine

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

def read_image(file_path):
    """从图片中提取文本内容"""
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def process_resume(file_path):
    """处理简历文件，自动判断文件类型并提取文本"""
    if file_path.endswith('.pdf'):
        resume_text = read_pdf(file_path)
    elif file_path.endswith('.docx'):
        resume_text = read_docx(file_path)
    elif file_path.endswith('.png'):
        resume_text = read_image(file_path)
    elif file_path.endswith('.jpg'):
        resume_text = read_image(file_path)
    elif file_path.endswith('.xlsx'):
        resume_data = pd.read_excel(file_path)  # 读取Excel文件
        resume_text = resume_data['职位期望'].values[0]  # 提取第一个列的值
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

tokenizer = BertTokenizer.from_pretrained('bert')
model = BertModel.from_pretrained('bert')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def main():
    # 加载并处理岗位信息
    jobs_df = pd.read_csv("data_all.csv").dropna(subset=['title', 'company', 'salary', 'education', 'description', 'address'])
    jobs_df['combined_info'] = jobs_df[['title', 'description']].apply(lambda x: ' '.join(x.astype(str)), axis=1)
    job_texts = jobs_df['combined_info'].tolist()

    job_embeddings = torch.load("jobs.pth")

    # 处理用户简历
    resume_text = process_resume("resumes/shen.pdf")  # 假设简历文件路径为 "path_to_resume.pdf"
    resume_embeddings = get_embeddings([resume_text])

    # 计算相似度并找到最匹配的岗位
    results = []
    for idx, job_emb in enumerate(job_embeddings):
        cos_sim = calculate_similarities(resume_embeddings, job_emb)
        results.append((jobs_df.iloc[idx]['company'], jobs_df.iloc[idx]['title'], cos_sim))

    # 排序找到最相似的岗位
    results.sort(key=lambda x: x[2], reverse=True)  # 基于相似度排序
    # 输出最相似的几个岗位信息
    for result in results[:10]:  # 只显示前5个最匹配的岗位
        print(f"公司: {result[0]}, 岗位: {result[1]}, 相似度: {result[2]}")

if __name__ == "__main__":
    main()
