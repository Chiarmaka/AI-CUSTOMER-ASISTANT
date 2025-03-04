# AI-CUSTOMER-ASISTANT

# Customer Support AI Chatbot

## Overview
This project is an AI-powered customer support chatbot that helps users with inquiries related to orders, shipping, refunds, product issues, discounts, and more. The chatbot uses a predefined knowledge base for instant responses and integrates with Google's Generative AI (Gemini) to generate responses for queries outside its knowledge base.

## Features
- **Predefined responses** for common customer queries.
- **AI-powered responses** using Google's Gemini model for complex or unknown queries.
- **Terminal-based chat interface** for testing the chatbot.
- **Configurable API key management** using `config.py` and environment variables.

## Project Structure
```
customer-support-bot/
│── agent.py         # Chatbot logic and AI model integration
│── config.py        # Manages API keys and environment variables
│── test.py          # Script to test the chatbot
│── main.py          # Entry point to run the chatbot
│── README.md        # Project documentation
```

## File Descriptions

### 1. `agent.py`
This file defines the `CustomerSupportBot` class, which:
- Loads the knowledge base from `knowledge_base.py`.
- Configures and interacts with the Gemini AI model.
- Determines whether to use predefined responses or AI-generated responses.
- Runs a chatbot interface in the terminal.

### 2. `config.py`
- Loads and manages API keys securely using environment variables.
- Contains a function `get_genai_model()` that initializes and configures the Gemini AI model.

### 3. `test.py`
- Contains test cases to verify chatbot responses for different user queries.
- Uses the `CustomerSupportBot` class to process sample questions and print responses.

### 4. `main.py`
- The entry point to launch the chatbot.
- Initializes the chatbot and starts a conversation loop in the terminal.

### 5. `requirements.txt`
- Lists dependencies required for the project, including:
  - `google-generativeai` (for Gemini API integration)
  - `python-dotenv` (for environment variable management)

## Installation
### Prerequisites
- Python 3.8+
- Google API Key for Gemini

### Steps to Set Up
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/customer-support-bot.git
   cd customer-support-bot
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up API Key:**
   - Create a `.env` file in the project root and add:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```
   - Alternatively, you can manually set it in `config.py`.

## Running the Chatbot
To start the chatbot in the terminal:
```sh
python main.py
```

To run tests:
```sh
python test.py
```

## Future Improvements
- Deploy as a web-based or chatbot API service.
- Integrate with a database for better customer support tracking.
- Implement natural language processing (NLP) to improve query understanding.

