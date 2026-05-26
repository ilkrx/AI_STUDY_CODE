import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# 1、加载文档
from langchain.document_loaders import TextLoader

loader = TextLoader("黑悟空.txt", encoding="utf-8")
docs = loader.load()

# 2、文档切块
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)

# 3、加载embedding模型
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5",model_kwargs={"device": "cpu"})

# 4、FAISS数据库初始化
from langchain_community.vectorstores import FAISS

vs = FAISS.from_documents(chunks, embedding)
context = vs.similarity_search("黑熊精自称为什么？")
print("rerank前:", context)

# rerank 重排
pairs = [["黑熊精自称为什么？", c.page_content] for c in context]
# print("----------------------")
# print(pairs)

import torch

device = "cpu" if torch.cuda.is_available() else "cpu"
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("models/AI-ModelScope/bge-reranker-v2-m3")
model = AutoModelForSequenceClassification.from_pretrained("models/AI-ModelScope/bge-reranker-v2-m3").to(device)
model.eval()

with torch.no_grad():
    # pairs:[[query, context],[]]
    # 对输入的文本进行编码
    inputs = tokenizer(pairs, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
    # 推理
    scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
    res = sorted([(pair[:][1], score) for pair, score in zip(pairs, scores)], key=lambda x: x[1], reverse=True)
    print(res)