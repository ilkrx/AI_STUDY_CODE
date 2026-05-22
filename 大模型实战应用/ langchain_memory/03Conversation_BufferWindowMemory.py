from langchain_openai import ChatOpenAI

# API密钥，基础的URL
api_key = "sk-yypoyhjaqtwojwhagprmshwmbkapglnbhivnrgpbudgbljli"
base_url = "https://api.siliconflow.cn/v1"

chat_model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=api_key,
        base_url=base_url,
)

from langchain_core.prompts import PromptTemplate

template = """
你是一个与人类对话的机器人。
{chat_history}

Human:{human_input}
Chatbot:
"""

prompt = PromptTemplate(input_variables=["chat_history", "human_input"], template=template)

from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(memory_key="chat_history", k=2)

from langchain.chains import LLMChain

llm_chain = LLMChain(llm=chat_model, prompt=prompt, verbose=True, memory=memory)

print(llm_chain.predict(human_input="可以介绍一下北京吗？"))
print(llm_chain.predict(human_input="北京有什么好玩的？"))
print(llm_chain.predict(human_input="故宫在哪里？"))
print(llm_chain.predict(human_input="北京有什么好吃的？"))