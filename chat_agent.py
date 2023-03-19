from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent


class ChatBot:
    def __init__(self, memory, agent_chain):
        self.memory = memory
        self.agent = agent_chain


def create_chatbot(model_name):
    search = GoogleSearchAPIWrapper()
    tools = [
        Tool(
            name="Current Search",
            func=search.run,
            description="useful for all question that asks about live events",
        ),
        Tool(
            name="Topic Search",
            func=search.run,
            description="useful for all question that are related to a particular topic, product, concept, or service",
        )
    ]
    memory = ConversationBufferMemory(memory_key="chat_history")
    chat = ChatOpenAI(temperature=0, model_name=model_name)
    agent_chain = initialize_agent(tools, chat, agent="conversational-react-description", verbose=True, memory=memory)

    return ChatBot(memory, agent_chain)