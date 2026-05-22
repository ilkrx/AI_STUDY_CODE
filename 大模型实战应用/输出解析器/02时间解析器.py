from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=api_key,
    base_url=base_url,
)

from langchain.output_parsers import DatetimeOutputParser
from langchain_core.prompts import PromptTemplate

parser = DatetimeOutputParser()
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
print("format_instructions:", parser.get_format_instructions())

formatted_prompt = prompt.format(query="北京奥运会是什么时候开幕的？")

response = chat_model.invoke(formatted_prompt).content
print(response)
output = parser.parse(response)
print("output:", output)