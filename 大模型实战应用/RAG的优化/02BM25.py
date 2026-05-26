# # pip install rank-bm25
# from rank_bm25 import BM25Okapi
#
# docs = [
#     "我 喜欢 吃 苹果",
#     "苹果 是 水果",
#     "苹果 手机 不错"
# ]
#
# # 预处理，将每个文档分词
# tokenized_doc = [doc.split() for doc in docs]
#
# # 初始化BM25
# bm25 = BM25Okapi(tokenized_doc)
#
# query = "我 喜欢 苹果".split()
#
# # 计算BM25
# bm25_scores = bm25.get_scores(query)
#
# print(f"{query} 在每篇文档中的BM25分数为")
# for idx, score in enumerate(bm25_scores):
#     print(f"第{idx + 1}篇文档的BM25分数为{score:.2f}")

# BM25
import math
from collections import Counter

# BM25参数
k1 = 1.5
b = 0.75

# 文档集
documents = [
    "我 喜欢 吃 苹果",
    "苹果 是 水果",
    "苹果 手机 不错"
]


# 预处理：将每个文档分词
def preprocess(document):
    return document.split()


# 计算词频（TF）
def compute_tf(document):
    word_count = Counter(document)
    return word_count


# 计算逆文档频率（IDF）
def compute_idf(documents):
    total_docs = len(documents)
    idf_dict = {}
    negative_idfs = []
    idf_sum = 0
    epsilon = 0.25
    all_words = set(word for doc in documents for word in doc)

    for word in all_words:
        doc_count = sum(1 for doc in documents if word in doc)
        idf_dict[word] = math.log((total_docs - doc_count + 0.5) / (doc_count + 0.5))
        # 以下部分是为了和库函数结果保持一致，实际作用就是将小于0的idf变成大于0的。
        idf_sum += idf_dict[word]
        if idf_dict[word] < 0:
            negative_idfs.append(word)
    average_idf = idf_sum / len(idf_dict)
    eps = epsilon * average_idf
    for word in negative_idfs:
        idf_dict[word] = eps
    return idf_dict


# 计算BM25
def compute_bm25(tf, idf, doc_len, avgdl):
    bm25 = {}
    for word, tf_value in tf.items():
        numerator = tf_value * (k1 + 1)
        denominator = tf_value + k1 * (1 - b + b * (doc_len / avgdl))
        bm25[word] = idf[word] * (numerator / denominator)
    return bm25


# 主程序
processed_docs = [preprocess(doc) for doc in documents]
tf_list = [compute_tf(doc) for doc in processed_docs]
idf = compute_idf(processed_docs)

# 计算文档的平均长度
doc_lengths = [len(doc) for doc in processed_docs]
avgdl = sum(doc_lengths) / len(documents)

# 输出每个文档的BM25值
for i, tf in enumerate(tf_list):

    bm25 = compute_bm25(tf, idf, len(processed_docs[i]), avgdl)
    print(f"文档 {i + 1} 的 BM25 值：")
    for word, value in bm25.items():
        print(f"{word}: {value:.4f}")