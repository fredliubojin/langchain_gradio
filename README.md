# fredliu-langchain-cse 🚀

Welcome to the **fredliu-langchain-cse** project! 🎉 This is a modern and sophisticated
chatbot powered by OpenAI's GPT-4, Gradio, and Google Custom Search API, designed to make
your life easier and more enjoyable. We're excited to have you here, and we hope you'll
consider contributing to this awesome project! 😃

## Features & Roadmap 💡

- [x] GPT-4 powered chatbot 🤖
- [x] Conversation history tracking 📜
- [x] Google Custom Search API integration 🔍
- [x] Easy-to-use Gradio interface 👩‍💻
- [x] Customizable agent chain 🛠️
- [ ] Add more tools to the agent chain
- [ ] Implement user authentication for API key management
- [ ] Create a web-based user interface
- [ ] Add support for multiple languages
- [ ] Integrate with popular messaging platforms

## Installation

1. Clone this repository:

```
git clone https://github.com/yourusername/fredliu-langchain-cse.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Set up your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY="your_openai_api_key"
```

4. Create a [Google Programmable Search](https://programmablesearchengine.google.com) engine and copy the ID.

5. Enable the Custom Search API in your [GCP console](https://console.cloud.google.com/apis/api/customsearch.googleapis.com),  
   and create a GCP API key [here](https://console.cloud.google.com/apis/credentials).

6. Set up the `GOOGLE_CSE_ID` and `GCP_API_KEY` environment variable:

```
export GOOGLE_CSE_ID="your_google_cse_id"
export GCP_API_KEY="your_gcp_api_key"
```

## Usage

1. Run the chatbot script:

```
python chatbot.py
```

2. Open the Gradio interface in your web browser and start chatting with the bot!

## Contributing

We would love for you to contribute to this project! 🤗 If you have any ideas, suggestions,
or improvements, please feel free to submit a pull request or open an issue.