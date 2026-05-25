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

# 导入ragas的嵌入模型包装器，用于将文本转换为向量表示
from ragas.embeddings import LangchainEmbeddingsWrapper
# 导入HuggingFace的嵌入模型实现，用于本地文本向量化
from langchain_huggingface import HuggingFaceEmbeddings

# 创建嵌入模型实例，加载本地的bge-large-zh-v1.5中文嵌入模型
embedding = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5"))

# 计算响应相关性
from ragas import SingleTurnSample
from ragas.metrics import ResponseRelevancy

sample = SingleTurnSample(
    user_input="故宫位于哪里?",
    response="故宫在北京"
)
scorer = ResponseRelevancy(llm=chat_model, embeddings=embedding)
print(scorer.single_turn_score(sample))