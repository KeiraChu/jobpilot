from transformers import BertTokenizer, BertModel
import torch
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
import time

tokenizer = BertTokenizer.from_pretrained('bert')
model = BertModel.from_pretrained('bert')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def read_file(file_path):
    """读取并返回文件的每行内容"""
    with open(file_path, encoding='utf-8') as f:
        return f.read().strip().split('\n')

def get_embeddings(texts, batch_size=4096):
    """批量获取文本的嵌入向量"""
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        
        time_1 = time.time()
        inputs = tokenizer(batch_texts, padding=True, truncation=True, return_tensors="pt", max_length=16)
        print(f"The time now single is {time.time() - time_1}")
        
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            time_1 = time.time()
            outputs = model(**inputs)
        
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        all_embeddings.extend(embeddings)
    
    return np.array(all_embeddings)

def calculate_similarities(embedding, embeddings):
    """计算向量与向量集合之间的余弦相似度"""
    if embedding.ndim > 1:
        embedding = embedding.squeeze()
    if embedding.shape[0] != embeddings.shape[1]:
        # 确保embedding形状与embeddings兼容
        raise ValueError("Embedding shapes are not compatible for dot product.")
    
    norms_embedding = np.linalg.norm(embedding)
    norms_embeddings = np.linalg.norm(embeddings, axis=1)
    cos_sim = np.dot(embeddings, embedding) / (norms_embeddings * norms_embedding)
    return cos_sim

def main():
    jobs_df = pd.read_csv("data_all.csv").dropna(subset=['title', 'company', 'salary', 'education', 'description', 'address'])
    # job_descriptions = jobs_df['description'].tolist()
    job_embeddings = torch.load("job.pth")
    # import ipdb; ipdb.set_trace()
    
    start_time = time.time()

    # 读取并处理用户信息
    info_types = ['工作任务', '技术栈', '福利', '要求']
    user_info = {info_type: read_file(info_type) for info_type in info_types}
    user_embeddings = {key: get_embeddings(texts) for key, texts in user_info.items()}

    # 读取岗位信息


    results = []
    for idx, job_emb in enumerate(job_embeddings):
        for info_type, embeddings in user_embeddings.items():
            cos_sim = calculate_similarities(job_emb, embeddings)
            max_similarity = np.max(cos_sim)
            if max_similarity > 0.95:
                results.append({
                    '公司': jobs_df.iloc[idx]['company'],
                    '岗位': jobs_df.iloc[idx]['title'],
                    
                    '匹配信息类型': info_type,
                    '相似度': max_similarity
                })

    print(f"Process completed in {time.time() - start_time:.2f} seconds.")
    
    results_df = pd.DataFrame(results)
    import ipdb; ipdb.set_trace()
    pd.DataFrame(results_df, columns=['sub_name', 'sub_type', 'obj_name', 'obj_type', 'rel_name', 'rel_type']).to_csv("rel—bert.csv", index=None)

    

if __name__ == "__main__":
    main()