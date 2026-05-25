import os
# 在导入任何深度学习库之前禁用CUDA
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# 导入LangChain的OpenAI聊天模型类，用于与LLM进行交互
from langchain_openai import ChatOpenAI


# API密钥配置，用于访问硅基流动平台的API服务
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
# 基础URL配置，指向硅基流动的API端点
base_url = "https://api.siliconflow.cn/v1"

# 创建聊天模型实例，使用DeepSeek-V3.2模型
# 初始化聊天大模型
chat_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",  # 指定使用的模型名称
    api_key=api_key,  # 传入API密钥进行身份验证
    base_url=base_url,  # 指定API的基础URL
)
# 初始化评估大模型
eval_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",  # 指定使用的模型名称
    api_key=api_key,  # 传入API密钥进行身份验证
    base_url=base_url,  # 指定API的基础URL
)

# 初始化嵌入模型
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5")

# 初始化提示词模板
from langchain_core.prompts import ChatPromptTemplate

system_prompt = "根据以下已知信息回答用户问题，\n 已知信息：{context}"
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "问题：{question}")
])

# 加载文档
from langchain_community.document_loaders import TextLoader

loader = TextLoader("黑悟空.txt", encoding="UTF-8")
docs = loader.load()

# 切片/分块
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)

# 使用FAISS做存储并得到检索器
from langchain_community.vectorstores import FAISS

vs = FAISS.from_documents(chunks, embedding)
retriever = vs.as_retriever()

# 初始化输出解析器
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

# 构建RAG链
from langchain_core.runnables import RunnablePassthrough

rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | chat_model
        | output_parser
)

# 导入csv文件，获得问题和标准回答
import pandas as pd

dataset = pd.read_csv("黑悟空.csv")

# 读取问题、真实答案字段、获取LLM的回答、获取上下文
questions = dataset["问题"].to_list()
ground_truths = dataset["回答"].to_list()

answers = []
contexts = []
for question in questions:
    answers.append(rag_chain.invoke(question))
    contexts.append([doc.page_content for doc in retriever.get_relevant_documents(question)])

# 创建输入ragas的数据
data = {
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "reference": ground_truths
}

# 构建输入RAGAS的数据集
from datasets import Dataset

dataset = Dataset.from_dict(data)

# 使用RAGAS进行RAG的评估
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

result = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
    llm=eval_model,
    embeddings=embedding
)

# 将测评结果显示出来
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)

df = result.to_pandas()
print(df)
