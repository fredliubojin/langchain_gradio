import gradio as gr
import openai
import os

def set_api_key(api_key):
    openai.api_key = api_key
    return "API Key set successfully."

def generate_response(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()

def chatbot(api_key, user_input, conversation_history=""):
    set_api_key(api_key)
    response = generate_response(user_input)
    updated_conversation = f"{conversation_history}\nUser: {user_input}\nChatbot: {response}\n"
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
