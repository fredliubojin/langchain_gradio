import gradio as gr
import openai

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
    return updated_conversation, response

api_key_input = gr.inputs.Textbox(lines=1, label="Enter OpenAI API Key")
user_input = gr.inputs.Textbox(lines=3, label="Enter your message")
conversation_history = gr.inputs.Textbox(lines=10, label="Conversation History")

output_history = gr.outputs.Textbox(label="Updated Conversation")
output_response = gr.outputs.Textbox(label="Chatbot Response")

iface = gr.Interface(
    fn=chatbot,
    inputs=[api_key_input, user_input, conversation_history],
    outputs=[output_history, output_response],
    title="GPT-4 Chatbot",
    description="A simple chatbot using GPT-4 and Gradio with conversation history",
)

iface.launch()
