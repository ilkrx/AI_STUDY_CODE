import os
# 在导入任何深度学习库之前禁用CUDA
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# 导入LangChain的OpenAI聊天模型类，用于与LLM进行交互
from langchain_openai import ChatOpenAI
# 导入ragas的LLM包装器，将LangChain的LLM转换为ragas可用的格式
from ragas.llms import LangchainLLMWrapper

# API密钥配置，用于访问硅基流动平台的API服务
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
# 基础URL配置，指向硅基流动的API端点
base_url = "https://api.siliconflow.cn/v1"

# 创建聊天模型实例，使用DeepSeek-V3.2模型，并通过LangchainLLMWrapper包装
chat_model = LangchainLLMWrapper(ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",  # 指定使用的模型名称
    api_key=api_key,  # 传入API密钥进行身份验证
    base_url=base_url,  # 指定API的基础URL
))

# 计算忠诚度
from ragas import SingleTurnSample
from ragas.metrics import Faithfulness

sample = SingleTurnSample(
    user_input="爱因斯坦出生于何时何地？",
    response="爱因斯坦于 1879 年 3 月 14 日出生于德国。",
    retrieved_contexts=[
        "阿尔伯特·爱因斯坦（Albert Einstein，生于 1879 年 3 月 14 日）是一位出生于德国的理论物理学家，被广泛认为是有史以来最伟大、最有影响力的科学家之一"],
)

scorer = Faithfulness(llm=chat_model)
print(scorer.single_turn_score(sample))