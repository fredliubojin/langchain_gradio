import gradio as gr
import openai
import os

import chat_agent
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def set_api_key(api_key):
    openai.api_key = api_key
    return "API Key set successfully."

def generate_response(prompt):
    agent = chat_agent.create_agent()
    response = agent.run(prompt)
    return response.strip()

def chatbot(api_key, user_input, conversation_history=""):
    set_api_key(api_key)
    response = generate_response(user_input)
    # Iterate through messages in ChatMessageHistory and format the output
    updated_conversation = ""
    for message in chat_agent.memory.chat_memory.messages:
        if isinstance(message, HumanMessage):
            prefix = "User: "
        else:
            prefix = "Chatbot: "
        updated_conversation += f"{prefix}{message.content}\n\n"
    return updated_conversation

# Get API key from environment variable OPENAI_API_KEY
api_key = os.environ.get("OPENAI_API_KEY")
api_key_input = gr.inputs.Textbox(lines=1, label="Enter OpenAI API Key", default=api_key)

user_input = gr.inputs.Textbox(lines=3, label="Enter your message")

output_history = gr.outputs.Textbox(label="Updated Conversation")

iface = gr.Interface(
    fn=chatbot,
    inputs=[api_key_input, user_input],
    outputs=[output_history],
    title="GPT-4 Chatbot",
    description="A simple chatbot using GPT-4 and Gradio with conversation history",
)

iface.launch()
