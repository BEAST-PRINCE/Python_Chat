Chatbot Script Using LangChain and Ollama

This script provides a simple chatbot interface using the LangChain library and Ollama's Llama3.1 model. It facilitates a conversation with the user, maintaining context throughout the interaction.
Features

    Interactive chat with the Llama3.1 language model.
    Maintains conversation context for coherent responses.
    Allows users to exit the chat with keywords like "exit," "bye," or "quit."

Prerequisites

    Python 3.8 or higher
    pip (Python package installer)

Setup Instructions
Step 1: Create a Virtual Environment

    Open a terminal or command prompt.

    Navigate to your project directory.

    Run the following command to create a virtual environment:

        python -m venv venv

    Activate the virtual environment:

        Windows:
            .\venv\Scripts\activate

        macOS/Linux:
            source venv/bin/activate

Step 2: Install Required Packages

    Ensure you have pip installed. If not, install it using:

    python -m ensurepip --upgrade

    Install the required packages:

        pip install langchain-core langchain-ollama

Step 3: Install Ollama and Pull the Llama3.1 Model

    Visit the Ollama website and follow the instructions to download and install the Ollama software appropriate for your operating system.

    Once installed, use pip to install the ollama package:

        pip install ollama

    Pull the Llama3.1 model:

        ollama pull llama3.1

Usage

    Run the script:

        python chatbot.py

    Follow the prompts to interact with the chatbot. Type your messages and press Enter to receive a response from the AI. To exit the chat, type "exit," "bye," or "quit."

