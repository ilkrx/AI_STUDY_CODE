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

# 从ragas指标模块导入上下文精度评估类，该类需要参考答案进行评估
from ragas.metrics._context_precision import LLMContextPrecisionWithReference

# 创建上下文精度评估器实例，传入之前配置的聊天模型
context_precision = LLMContextPrecisionWithReference(llm=chat_model)

# 导入ragas的单轮对话样本类，用于构造测试数据
from ragas import SingleTurnSample

# 创建一个单轮对话样本，包含用户输入、模型响应、参考答案和检索到的上下文
sample = SingleTurnSample(
    user_input="故宫位于哪里？",  # 用户的提问内容
    response="故宫在北京。",  # LLM生成的回答内容
    reference="故宫位于北京。",  # 真实的标准答案，用于对比评估
    retrieved_contexts=["北京是中国的首都", "故宫位于北京"]  # 从知识库中检索到的相关上下文信息
)

# 计算并打印该样本的上下文精度得分，评估检索内容与参考答案的相关性
print(context_precision.single_turn_score(sample))