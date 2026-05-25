# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer("models/AI-ModelScope/bge-large-zh-v1___5")
#
# texts = ["院子里有一只可爱的小猫", "厨房里有一只黑色的猫",  "大模型真简单"]
#
# embs = model.encode(texts)
#
# from sklearn.metrics.pairwise import cosine_similarity
# print(cosine_similarity([embs[0]], [embs[1]]))
# print(cosine_similarity([embs[0]], [embs[2]]))

import os
# 在导入任何深度学习库之前禁用CUDA
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5")

texts = ["院子里有一只可爱的小猫", "厨房里有一只黑色的猫", "大模型真简单"]

from langchain_community.vectorstores import FAISS

# 构建FAISS 向量存储和retriever
vs = FAISS.from_texts(texts=texts, embedding=model)
print(vs.similarity_search("黑色的猫在哪里？"))