from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent

search = GoogleSearchAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for all question that asks about live events",
    ),
    Tool(
        name = "Topic Search",
        func=search.run,
        description="useful for all question that are related to a particular topic, product, concept, or service",
    )
]
memory = ConversationBufferMemory(memory_key="chat_history")
llm=OpenAI(temperature=0, model_name="text-davinci-003")

def create_agent():
    agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)
    return agent_chain


