@'
# Smart Budget Tracker 💰

A full‑stack budget management app built with **FastAPI + React + Chakra UI**.  
Designed for recruiter demos with polished UI, seeded demo data, and secure authentication.

## 🚀 Features
- 🔐 Secure login/signup with JWT
- 🌓 Light/Dark theme toggle
- 👤 Manage Account (email, phone, location)
- 💳 Accounts overview
- 📊 Budgets by category
- 💸 Transactions history

## 🎯 Demo Login
- Email: `demo@budget.com`
- Password: `demo123`

## 🛠️ Tech Stack
- Backend: FastAPI, SQLAlchemy, Alembic, PostgreSQL
- Frontend: React, TypeScript, Chakra UI
- Auth: JWT secure flows

## 📦 Setup
```bash
# Backend
cd backend
poetry install
poetry run uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
