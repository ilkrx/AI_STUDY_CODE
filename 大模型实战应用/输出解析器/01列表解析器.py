from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="Qwen/Qwen2.5-7B-Instruct",
    api_key=api_key,
    base_url=base_url,
)

from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

# 实例化：逗号分隔的列表解析器
parser = CommaSeparatedListOutputParser()
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

print("format_instructions: ", parser.get_format_instructions())
formatted_prompt = prompt.format(query="列出五种水果。")

print("formatted_prompt:", formatted_prompt)

# 生成响应
response = chat_model.invoke(formatted_prompt).content
print(response)

# 解析响应
output = parser.parse(response)
print("output:", output)