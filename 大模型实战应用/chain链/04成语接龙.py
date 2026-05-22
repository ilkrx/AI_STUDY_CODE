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

prompt = ChatPromptTemplate.from_template("""
接下来的四字成语必须以上一个成语“{pre_cy}”的最后一个字为开头。
例如：上一个成语是“兴高采烈”，那么下一个成语应该是以“烈”开头的成语。
请给出成语“{pre_cy}”接下来的接龙成语：
""")

# 创建一个字符串输出解析器
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

# 构造一个链，依次包含提示模板、语言模型，输出解析器
chain = prompt | chat_model | output_parser

while True:
    cy = input("给出成语：")
    init_cy = cy
    print("AI回答：", chain.invoke({"pre_cy": init_cy}))