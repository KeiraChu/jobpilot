import jieba #用于中文分词
import pandas as pd
import re
import numpy as np
import time
from gensim.models.doc2vec import TaggedDocument, Doc2Vec


time_0 = time.time()
# 读取工作任务、技术栈、福利和要求的文本文件
gzrw = open("工作任务", encoding="utf-8").read().strip().split("\n")
jsz = open("技术栈", encoding="utf-8").read().strip().split("\n")
fl = open("福利", encoding="utf-8").read().strip().split("\n")
yq = open("要求", encoding="utf-8").read().strip().split("\n")

# 加载已训练好的Doc2Vec模型
model = Doc2Vec.load("doc2vec.model")
# model = Doc2Vec(vector_size=2000)

# 根据文本文件中的内容生成对应的向量
gzrw_vector = [model.infer_vector(list(jieba.cut(i))) for i in gzrw]
jsz_vector = [model.infer_vector(list(jieba.cut(i))) for i in jsz]
fl_vector = [model.infer_vector(list(jieba.cut(i))) for i in fl]
yq_vector = [model.infer_vector(list(jieba.cut(i))) for i in yq]

# 读取数据文件并删除空值
t = pd.read_csv("data_all.csv").dropna(subset=['title', 'company', 'salary', 'education', 'description', 'address'])
rel = []

# 对每条数据进行处理
for i, row in t.iterrows():
    rel.append([row['company'] + row['title'], '公司具体岗位',row['title'], '招聘名称', '职位名称', '职位名称'])
    rel.append([row['company'] + row['title'], '公司具体岗位', row['salary'], '薪资水平', '工作薪资', '工作薪资'])
    rel.append([row['company'] + row['title'], '公司具体岗位', row['education'], '学历要求', '工作学历', '工作学历'])
    rel.append([row['company'] + row['title'], '公司具体岗位', row['address'], '地址', '工作地址', '工作地址'])
    # 将描述字段按照标点符号切分为多个句子
    desc = re.split("[、，。？~；【】（）{}-·,.?!;,\(\)\[\]\{\}\+]", row['description'])
    desc = [model.infer_vector(list(jieba.cut(i))) for i in desc]

    rel.append([row['company'] + row['title'], '公司具体岗位', row['company'], '公司', '相关公司', '相关公司'])
    rel.append([row['company'] + row['title'], '公司具体岗位', row['title'], '岗位名称', '相关岗位', '相关岗位'])
    # 对每个句子的向量与关键词向量进行相似度计算
    for ii in desc:
        for index, j in enumerate(gzrw_vector):  # 遍历"工作任务"关键词向量列表，其中index是当前关键词向量的索引，j是当前关键词向量。
            v1 = np.sqrt(ii.dot(ii))  # 计算描述文本句子向量ii的模长，即欧几里得范数。
            v2 = np.sqrt(j.dot(j))  # 计算当前关键词向量j的模长。
            cos = ii.dot(j) / (v1 * v2)  # 计算描述文本句子向量和当前关键词向量的余弦相似度。余弦相似度是通过两个向量之间的点积除以它们的模长的乘积得到的。
            if cos > 0.95:  # 如果余弦相似度大于0.95，说明描述文本句子与当前关键词向量的相似度较高。
                rel.append([row['company']+row['title'], '公司具体岗位', gzrw[index], '工作任务', '工作任务', '工作任务'])  # 将相关信息添加到rel列表中，包括标题、关系类型、关键词名称和关系名称。
                break
        for index, j in enumerate(jsz_vector):
            v1 = np.sqrt(ii.dot(ii))
            v2 = np.sqrt(j.dot(j))
            cos = ii.dot(j) / (v1 * v2)
            if cos > 0.95:
                rel.append([row['company']+row['title'], '公司具体岗位', jsz[index], '技术栈', '技术栈', '技术栈'])
                break
        for index, j in enumerate(fl_vector):
            v1 = np.sqrt(ii.dot(ii))
            v2 = np.sqrt(j.dot(j))
            cos = ii.dot(j) / (v1 * v2)
            if cos > 0.95:
                rel.append([row['company']+row['title'], '公司具体岗位', fl[index], '福利', '工作福利', '工作福利'])
                break

        for index, j in enumerate(yq_vector):
            v1 = np.sqrt(ii.dot(ii))
            v2 = np.sqrt(j.dot(j))
            cos = ii.dot(j) / (v1 * v2)
            if cos > 0.95:
                rel.append([row['company']+row['title'], '公司具体岗位', yq[index], '要求', '工作要求', '工作要求'])
                break
    print(i, row)

# 将结果保存为Excel文件
pd.DataFrame(rel, columns=['sub_name', 'sub_type', 'obj_name', 'obj_type', 'rel_name', 'rel_type']).to_csv("rel.csv", index=None)
print(f"The time consumed is {time.time()- time_0}")
