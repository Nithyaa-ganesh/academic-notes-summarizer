# Academic Notes Summarizer

Welcome to the **Academic Notes Summarizer**! This is a simple yet powerful web application that helps you upload your academic notes, extract the text, generate summaries, flashcards, and even mind maps to help you study more effectively. It also allows you to download all the generated content in a PDF format so you can have it handy wherever you go!

## Key Features

- **Easy Upload**: Upload your academic notes in PDF or DOCX format with just a few clicks.
- **Text Extraction**: We automatically extract the text from your notes for easy processing.
- **Smart Summarization**: Using advanced AI, your notes are summarized to highlight key concepts and important information.
- **Flashcards**: We generate helpful flashcards based on the summary to aid your studying process.
- **Mind Maps**: Visual learners will love this feature! We turn the key concepts into a mind map for better understanding.
- **PDF Export**: Once you're done, you can download everything—summary, flashcards, and mind map—in a neat PDF file to keep for future reference.
- **Live on Hugging Face Spaces**: The app is deployed on Hugging Face Spaces, making it accessible from anywhere!

##  Tech Stack

- **Frontend**: Streamlit – Fast, beautiful UI for an effortless user experience.
- **Backend**: Python – The brains behind the operation.
- **AI/ML**: Langflow – We use powerful language models to handle summarization and other AI tasks.
- **Deployment**: Hugging Face Spaces – For easy access and fast deployment.

## Prerequisites

Before running this project, make sure you have the following:

- Python 3.x
- Streamlit
- Langflow
- Hugging Face API key (for using AI models)
- Python-dotenv (to securely store your API keys)

Install Dependencies
Install all the required libraries:
    pip install -r requirements.txt

Add Your API Keys
Run the Application:
    streamlit run app.py
