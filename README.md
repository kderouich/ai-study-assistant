# AI Study Assistant

AI-powered study assistant backend built with FastAPI and OpenRouter.

## Features

* Ask AI for topic explanations
* Generate quizzes
* Evaluate quiz answers

## Tech Stack

* Python
* FastAPI
* OpenRouter
* Pydantic

## Project Structure

```text
app/
│── main.py
├── models/
├── routes/
└── services/
```

## Installation

```bash
git clone <your-repo-url>
cd ai-study-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate venv:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```
