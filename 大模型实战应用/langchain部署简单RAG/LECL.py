from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=api_key,
    base_url=base_url,
)

from langchain_community.document_loaders import TextLoader

loader = TextLoader("黑悟空.txt", encoding="utf-8")
docs = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter

# 块大小200字为一组，每组之间20字重叠
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)  # 分割成块

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5", model_kwargs={"device": "cpu"})

# 构建faiss向量存储
from langchain_community.vectorstores import FAISS

vs = FAISS.from_documents(chunks, embedding)  # 将文本块转换为向量并且存储到FAISS

retriever = vs.as_retriever()  # 创建检索器用于从数据库中获取相关信息

from langchain.chains import RetrievalQA
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_msg = SystemMessagePromptTemplate.from_template(
    "根据以下已知的内容回答用户问题。\n  已知消息{context}"
)

huamn_msg = HumanMessagePromptTemplate.from_template(
    "用户问题：{question}"
)

chat_prompt = ChatPromptTemplate.from_messages([
    system_msg, huamn_msg
])

"""使用LECL实现"""


# 格式化文档，将多个文档连接成一个
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# 创建字符串输出解析器，用于解析LLM的输出
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

from langchain_core.runnables import RunnablePassthrough

# 创建 rag_chain 
rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}  # 构建上下文字典
        | chat_prompt
        | chat_model
        | output_parser
)
print(rag_chain.invoke("黑熊精自称为？"))