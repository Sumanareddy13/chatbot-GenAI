# AI-Powered Personal Study Assistant

An interactive web application built with **Streamlit** and **Hugging Face Transformers** that serves as a personal AI study assistant. The app supports multiple NLP tasks such as question answering, summarization, translation, and text generation.

## Features

- **Question Answering**: Ask questions and get answers based on the input context.
- **Summarization**: Generate concise summaries of long texts.
- **Translation**: Translate English text to French.
- **Text Generation**: Generate creative text based on a prompt.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers (with models like DistilBERT and GPT-2)
- PyTorch (backend for transformer models)

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Sumanareddy13/chatbot-GenAI.git
   ```

2. ## Navigate to project folder

   cd chatbot-GenAI

3. ## Create and activate a virtual environment

   python -m venv study_env_310
   source study_env_310/bin/activate  
   On Windows:study_env_310\Scripts\activate

4. ## Install dependencies:

   pip install -r requirements.txt

5. ## Run the Steamlit app:
   streamlit run app.py
