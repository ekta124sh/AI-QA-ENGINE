# 🤖 AI QA Engine

An AI-powered Quality Assurance platform that automates the software testing lifecycle by generating intelligent test cases, Playwright automation scripts, executing tests, and providing interactive dashboards and reports.

---

## 📌 Project Overview

AI QA Engine is a full-stack web application developed to simplify and accelerate software testing using Artificial Intelligence. The platform enables QA engineers to manage projects, generate AI-based test cases, create Playwright automation scripts, execute tests, and analyse reports from a single dashboard.

---

## 🚀 Features

- 🔐 JWT Authentication (Login & Registration)
- 📁 Project Management
- 🤖 AI Test Case Generation
- 🎭 Playwright Script Generation
- ▶️ Test Execution Dashboard
- 📊 Interactive Analytics Dashboard
- 📈 Execution Trend Charts
- 📄 PDF Report Export
- 📊 Excel Report Export
- 📑 Allure Report Download
- 🎨 Material UI Responsive Design
- 🔔 Snackbar Notifications
- 🚪 Logout Confirmation Dialog
- ❌ Custom 404 Page

---

## 🛠 Tech Stack

### Frontend

- React 19
- TypeScript
- Material UI
- Redux Toolkit
- React Router
- Axios
- Recharts
- Vite

### Backend

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pydantic

### Automation

- Playwright
- AI Generated Test Cases

---

## 📂 Project Structure

```
AI-QA-ENGINE
│
├── backend
│   ├── api
│   ├── services
│   ├── models
│   ├── database
│   ├── utils
│   └── reports
│
├── frontend
│   ├── components
│   ├── pages
│   ├── services
│   ├── layouts
│   ├── context
│   └── assets
│
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Authentication

- Register New User
- Login using JWT Authentication
- Protected Routes
- Automatic Logout on Session Expiry

---

## Reports

- PDF Export
- Excel Export
- Allure Report

---

## Future Enhancements

- Role Based Access Control
- Email Notifications
- Docker Deployment
- CI/CD Integration
- GitHub Actions
- AI Chat Assistant
- Multi-user Collaboration

---

## Developed By

Ashish Golwa

Senior QA Engineer | Automation Engineer

Technologies:
Python | FastAPI | React | TypeScript | PostgreSQL | Playwright | Material UI