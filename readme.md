# Teza - Music Memory Submission

This is a small hands-on app built as part of the Teza full-stack home assignment.

The app allows users to submit a memory about a band from a specific year and why they like them. The backend generates a short description and image using OpenAI’s GPT and DALL·E, and stores the latest submission locally.

## 🛠️ Tech Stack

- **Frontend:** React + Tailwind CSS
- **Backend:** FastAPI (Python)
- **AI Integration:** OpenAI (GPT-3.5 & DALL·E)
- **Storage:** JSON file as local DB - submissions.json

## 🚀 Run Locally

### 1. Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI key - you can use my if there are credit left.
uvicorn backend.main:app --reload
