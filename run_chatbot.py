import hupper
import chatbot

if __name__ == '__main__':
    reloader = hupper.start_reloader('chatbot.main')  # Replace 'your_gradio_app.main' with the function that launches your Gradio app
    chatbot.main()