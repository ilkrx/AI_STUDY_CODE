from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=api_key,
    base_url=base_url,
)

# 创建聊天模板，包含占位符topic
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("说出一句包含{topic}的诗句")

# 创建一个字符串输出解析器
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

# 构造一个链，依次包含提示模板、语言模型，输出解析器
chain = prompt | chat_model | output_parser

print(chain.invoke({"topic": "花"}))