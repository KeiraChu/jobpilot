import pandas as pd
import jieba
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
import numpy as np

t = pd.read_csv("data_all.csv")['description']
# 对每个描述进行中文分词，并将结果存储在processed_docs列表中
processed_docs = [list(jieba.cut(i)) for i in t]
# 为每个描述创建一个标签，将中文分词结果和标签存储在tagged_data列表中
tagged_data = [TaggedDocument(words=doc, tags=[str(i)]) for i, doc in enumerate(processed_docs)]

# 创建一个Doc2Vec模型，向量维度为50，最小词频为2，迭代次数为100
model = Doc2Vec(vector_size=50, min_count=2, epochs=100)
# 在模型中构建词汇表
model.build_vocab(tagged_data)
# 使用标记的数据训练模型
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
# 将训练好的模型保存到文件中
model.save("doc2vec.model")