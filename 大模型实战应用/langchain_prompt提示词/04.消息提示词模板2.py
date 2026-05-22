from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_message = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个有用的助手，你会帮助用户学习编程。"),
    HumanMessage(content="用户问：如何开始学习python？"),
    AIMessage(content="")
])

print(chat_message.format_messages())