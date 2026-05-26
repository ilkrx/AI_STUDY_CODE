import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# 定义文档列表
documents = [
    "python 是一种广泛使用的编程语言",
    "JavaScript 被广泛应于WEB开发",
    "机器学习是人工智能的一个分支",
    "FAISS 是一个高校的向量相似度检索库",
    "BM25 是一种常用于信息检索的评分函数"
]

import jieba

# 预处理，将每个文档分词
tokenized_corpus = [list(jieba.cut(doc.lower())) for doc in documents]
# print(tokenized_corpus)

from rank_bm25 import BM25Okapi

# 初始化BM25
bm25 = BM25Okapi(tokenized_corpus)

from langchain_community.embeddings import HuggingFaceEmbeddings

# 初始化嵌入模型
embedding = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5",model_kwargs={"device": "cpu"})

from langchain_community.vectorstores import FAISS

# 构建FAISS检索器
vs = FAISS.from_texts(documents, embedding)
# 相似度检索
faiss_retriver = vs.as_retriever(search_kwargs={"k": 2})

from langchain_community.retrievers import BM25Retriever

bm25_retriever = BM25Retriever.from_texts(documents)
bm25_retriever.k = 2
bm25_retriever.vectorizer = bm25

from langchain.retrievers import EnsembleRetriever

# 构建混合检索
ensemble_retirver = EnsembleRetriever(
    retrievers=[faiss_retriver, bm25_retriever],
    weights=[0.5, 0.5]
)

# 使用混合检索器进行检索
docs = ensemble_retirver.invoke("python")
# print(docs)
page_contents = [doc.page_content for doc in docs]
print(page_contents)