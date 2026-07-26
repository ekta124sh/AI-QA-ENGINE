# 🚀 AI QA Engine

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![React](https://img.shields.io/badge/React-19-blue?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Playwright](https://img.shields.io/badge/Playwright-Automation-brightgreen?logo=playwright)
![Material UI](https://img.shields.io/badge/Material_UI-Frontend-blue?logo=mui)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 📌 Overview

AI QA Engine is an enterprise-grade AI-powered test automation platform that automatically analyses software repositories, generates intelligent test cases using Large Language Models (LLMs), creates Playwright automation scripts, executes test suites, and provides interactive dashboards with downloadable reports.

The platform combines modern backend architecture, AI services, and an intuitive frontend to significantly reduce manual QA effort.

---

# ✨ Features

✅ AI-powered Test Case Generation

✅ Playwright Script Generation

✅ Repository Analysis

✅ Intelligent Endpoint Detection

✅ Authentication Detection

✅ Dashboard Analytics

✅ JWT Authentication

✅ Project Management

✅ Execution History

✅ PDF Report Export

✅ Excel Report Export

✅ Allure Report Support

✅ PostgreSQL Database

✅ Multiple LLM Providers

- Google Gemini
- Groq
- OpenRouter

---

# 🛠 Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| Frontend | React + Vite |
| Language | Python, TypeScript |
| Database | PostgreSQL |
| Authentication | JWT |
| AI Providers | Gemini, Groq, OpenRouter |
| Automation | Playwright |
| UI | Material UI |
| Charts | Recharts |
| Reports | PDF, Excel, Allure |
| Version Control | Git + GitHub |

---

# 🏗 Project Architecture

```text
                    +-----------------------+
                    |      React UI         |
                    |  Material UI + Vite   |
                    +----------+------------+
                               |
                               |
                     REST APIs (JWT)
                               |
                               ▼
                 +--------------------------+
                 |       FastAPI API        |
                 +--------------------------+
                 | Authentication           |
                 | Dashboard APIs          |
                 | Project APIs            |
                 | Test Case APIs          |
                 | Playwright APIs         |
                 +------------+------------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          ▼                   ▼                   ▼
 Repository Analyzer     AI Engine         Report Engine
          |                   |                   |
          |             Gemini/Groq/OpenRouter    |
          |                   |                   |
          +-------------------+-------------------+
                              |
                              ▼
                       PostgreSQL Database
```

---

# 📂 Project Structure

```text
AI_QA_ENGINE
│
├── backend
│   ├── agents
│   ├── ai
│   ├── analyzers
│   ├── api
│   ├── auth
│   ├── config
│   ├── context
│   ├── database
│   ├── llm
│   ├── models
│   ├── prompts
│   ├── schemas
│   ├── services
│   ├── tests
│   └── utils
│
├── ai-qa-frontend
│   ├── src
│   ├── public
│   ├── assets
│   └── components
│
├── docker
├── docs
├── generated_reports
├── generated_tests
├── repositories
├── requirements.txt
└── README.md
```

---

# 🔄 Workflow

```text
Repository URL
      │
      ▼
Clone Repository
      │
      ▼
Repository Analysis
      │
      ▼
AI Context Builder
      │
      ▼
LLM (Gemini/Groq/OpenRouter)
      │
      ▼
Generate Test Cases
      │
      ▼
Generate Playwright Scripts
      │
      ▼
Execute Tests
      │
      ▼
Generate Reports
      │
      ▼
Dashboard Analytics
```

---

# 📊 Dashboard

The dashboard provides:

- Total Projects
- Total Test Cases
- Execution Statistics
- Pass / Fail Rate
- Recent Executions
- Execution Trend
- Project Analytics
- Test Coverage

---

# 📷 Screenshots

## Login

```
screenshots/login.png
```

---

## Dashboard

```
screenshots/dashboard.png
```

---

## Projects

```
screenshots/projects.png
```

---

## Test Case Generator

```
screenshots/testcases.png
```

---

## Playwright Generator

```
screenshots/playwright.png
```

---

## Reports

```
screenshots/reports.png
```

---

# ⚙ Installation

## Clone

```bash
git clone https://github.com/ekta124sh/AI-QA-ENGINE.git

cd AI-QA-ENGINE
```

---

## Backend

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Frontend

```bash
cd ai-qa-frontend

npm install

npm run dev
```

---

## Configure Environment

Create a `.env`

```env
APP_NAME=AI QA Engine

DB_HOST=

DB_PORT=

DB_NAME=

DB_USER=

DB_PASSWORD=

JWT_SECRET_KEY=

GROQ_API_KEY=

GEMINI_API_KEY=

OPENROUTER_API_KEY=
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

---

## Run Frontend

```bash
npm run dev
```

---

# 🔐 Authentication

JWT-based authentication is implemented.

Features include:

- User Registration
- Login
- Secure Password Hashing
- Protected APIs
- Token Validation

---

# 📈 Future Enhancements

- Azure OpenAI Integration
- GitHub Actions
- Jenkins Pipeline
- CI/CD Automation
- Selenium Support
- Cypress Support
- AI Bug Prediction
- Test Impact Analysis
- Slack Notifications
- Jira Integration

---

# 👨‍💻 Author

**Ekta Sharma**

GitHub

LinkedIn

Email

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub!
