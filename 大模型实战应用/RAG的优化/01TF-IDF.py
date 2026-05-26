# 使用sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "我 喜欢 吃 苹果",
    "苹果 是 水果",
    "苹果 手机 不错"
]

# token_pattern=r"(?u)\b\w+\b" 保留单个词
vector = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")

# 计算TF-IDF
tfidf = vector.fit_transform(docs)
print(vector.vocabulary_)
# 输出TF-IDF
print(tfidf.toarray())