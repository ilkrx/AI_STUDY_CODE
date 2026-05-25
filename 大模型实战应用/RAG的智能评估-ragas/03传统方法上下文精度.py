# 从ragas库中导入非LLM上下文精度评估类（基于传统方法的评估）
from ragas.metrics._context_precision import NonLLMContextPrecisionWithReference

# 创建上下文精度评估器实例
context_precision = NonLLMContextPrecisionWithReference()

# 从ragas库中导入单轮对话样本类
from ragas import SingleTurnSample

# 创建一个单轮对话样本，用于评估检索结果的准确性
sample = SingleTurnSample(
    retrieved_contexts=["故宫在北京"],  # 检索到的上下文列表
    reference_contexts=["故宫位于北京"]  # 参考的真实上下文列表
)

# 计算并打印该样本的上下文精度得分
print(context_precision.single_turn_score(sample))