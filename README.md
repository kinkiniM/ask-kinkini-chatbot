# Ask Kinkini Chatbot

Ask Kinkini is a personal portfolio chatbot built with **FastAPI**, **Streamlit**, and **Docker**.

It answers questions about Kinkini Majumdar’s professional experience, AI/ML work, data science skills, projects, services, pricing, and contact details.

## Features

* Chat interface using Streamlit
* FastAPI backend for chatbot response logic
* Fixed FAQ-based responses
* Keyword matching
* Suggested question buttons
* Contact details shown only when asked or when the bot does not know the answer
* CTA shown only when the user ends the conversation
* Dockerized frontend and backend
* Ready for deployment

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit
* Requests

### DevOps

* Docker
* Docker Compose

## Project Structure

```text
ask-kinkini-chatbot/
│
├── docker-compose.yml
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── faqs.py
│       └── chatbot.py
│
└── frontend/
    ├── Dockerfile
    ├── requirements.txt
    └── app/
        └── streamlit_app.py
```

## How It Works

The chatbot uses a simple FAQ-based matching system.

1. User asks a question from the Streamlit frontend.
2. The frontend sends the question to the FastAPI backend.
3. The backend checks the question against predefined FAQ keywords.
4. If a match is found, the bot returns the related answer.
5. If no match is found, the bot gives a fallback response with contact details.
6. After every answer, the bot asks if the user needs anything else.
7. If the user says no, the chatbot shows a final CTA.

## Run Locally with Docker

Make sure Docker Desktop is running.

From the root project folder, run:

```bash
docker compose up --build
```

Then open:

```text
Frontend:
http://localhost:8501

Backend:
http://localhost:8000

Backend health check:
http://localhost:8000/health
```

## Backend API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Chat Endpoint

```http
POST /chat
```

Request body:

```json
{
  "message": "What is your work experience?"
}
```

Example response:

```json
{
  "response": "Kinkini has professional experience across AI engineering, data analytics..."
}
```

## Example Questions

You can ask:

```text
Who are you?
```

```text
What is your work experience?
```

```text
What work have you done in Sampurna?
```

```text
For how many days have you worked for Sampurna?
```

```text
What work have you done in Capgemini?
```

```text
For how many days have you worked for Capgemini?
```

```text
What are your AI related skills?
```

```text
What are your data science skills?
```

```text
What RAG work have you done?
```

```text
What voice agent have you built?
```

```text
What services do you offer?
```

```text
How can I contact you?
```

## Main Use Case

This project works as an interactive portfolio assistant.

Instead of reading a full resume, recruiters, clients, and LinkedIn visitors can ask questions and quickly understand:

* Professional background
* AI/ML experience
* Data science skills
* Projects
* Services
* Contact details

## Future Improvements

Planned improvements:

* Add LLM fallback
* Add lead capture form
* Store leads in Google Sheets
* Add admin-editable FAQ file
* Add analytics for most asked questions
* Add better UI styling
* Add deployment-ready single Streamlit version
* Add authentication for admin updates

## Author

**Kinkini Majumdar**

AI Engineer / Python Developer with experience in LLM applications, RAG, conversational AI, FastAPI backends, data analytics, Power BI dashboards, and automation.

## Contact

Email: [kinkinimajumder@gmail.com](mailto:kinkinimajumder@gmail.com)

LinkedIn: https://www.linkedin.com/in/kinkini-majumdar-781b1b186/

GitHub: https://github.com/kinkiniM/