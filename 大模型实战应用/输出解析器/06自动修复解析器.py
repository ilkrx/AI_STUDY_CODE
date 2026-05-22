from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="Qwen/Qwen2.5-7B-Instruct",
    api_key=api_key,
    base_url=base_url,
)

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")


# 顶一个格式不正确的输出（注意：这个代表大模型的输出结果）
misformatted = "{'name': 'John', 'age': 30}"
parser = PydanticOutputParser(pydantic_object=Person)
try:
    output = parser.parse(misformatted)
    print("output:", output)
except Exception as e:
    print(e)

from langchain.output_parsers import OutputFixingParser

new_parser = OutputFixingParser.from_llm(parser=parser, llm=chat_model)
output = new_parser.parse(misformatted)
print("output:", output)