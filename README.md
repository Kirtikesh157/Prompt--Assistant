# 🤖 Prompt Engineering Assistant

An AI-powered Prompt Engineering Assistant built with **Python**, **Streamlit**, and the **Gemini API**. This application transforms simple, vague, or incomplete user requests into clear, detailed, and effective prompts for AI language models.

## Features

* Improve vague or incomplete prompts
* Generate well-structured prompts for LLMs
* Preserve the user's original intent
* Add relevant context and constraints
* Define the expected output format
* Interactive Streamlit web interface
* Powered by the Gemini API

## Tech Stack

* Python
* Streamlit
* google-genai
* Prompt Engineering
* python-dotenv

## Project Structure

```text
Prompt-Engineering-Assistant/
│── app.py
│── prompt_engineering_assistant.txt
│── requirements.txt
│── .env
│── image.png
└── README.md
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/Kirtikesh157/-Prompt-Engineering-Assistant
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
GEMINI_API_KEY=your_gemini_api_key
```

4. Run the application

```bash
streamlit run app.py
```

## Example

**Input**

```text
I need help building something with AI for students.
```

**Output**

The assistant transforms the request into a detailed, structured prompt by adding context, defining the role, specifying requirements, and formatting the expected output.

## Future Enhancements

* Multiple prompt templates
* Prompt history
* Export prompts to PDF or DOCX
* Multi-model support
* Dark/Light theme toggle

## Author

**Kirtikesh Bhoyar**

If you found this project useful, feel free to the repository.
