#  AI Software Engineering Agent Platform

> A production-style multi-agent AI platform that automates the software engineering workflow using **Python, LangGraph, FastAPI, and LLMs**.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)]()
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange.svg)]()
[![Tests](https://img.shields.io/badge/Tests-Pytest-success.svg)]()

---

##  Overview

Building software involves multiple stages: understanding requirements, planning the implementation, writing code, creating tests, and evaluating the final result.

This project automates that workflow using a **multi-agent architecture**.

A user submits a software requirement, and specialized AI agents collaborate to:

1.  Analyze the requirement
2.  Create a development plan
3.  Generate application code
4.  Generate test cases
5.  Evaluate the implementation

The agents are orchestrated using **LangGraph**, while **FastAPI** exposes the platform through REST APIs.

---

##  Architecture

```text
                    ┌──────────────────┐
                    │ User Requirement │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Planner Agent  │
                    │ Requirement → Plan│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Coder Agent   │
                    │ Plan → Code      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Tester Agent   │
                    │ Code → Test Cases│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Evaluator Agent  │
                    │ Validate Output  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Final Response  │
                    └──────────────────┘
```

---

##  Features

-  Multi-agent workflow orchestration using **LangGraph**
-  **Planner Agent** for requirement analysis and software planning
-  **Coder Agent** for generating application code
-  **Tester Agent** for generating test cases
-  **Evaluator Agent** for evaluating generated implementations
-  REST APIs built with **FastAPI**
-  LLM provider abstraction
-  Support for mock and OpenAI-based LLM providers
-  Automated testing using **Pytest**
-  Code quality checks using **Ruff**
-  Interactive API documentation with **Swagger UI**

---

##  Multi-Agent Workflow

| Agent | Responsibility |
|---|---|
|  Planner Agent | Analyzes requirements and creates a software development plan |
|  Coder Agent | Generates application code based on the development plan |
|  Tester Agent | Generates test cases for the implementation |
|  Evaluator Agent | Evaluates generated code and determines whether the implementation passes |

---

##  Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### AI & Agent Framework

- LangGraph
- LLM Providers
- OpenAI API

### Testing & Quality

- Pytest
- Pytest-Asyncio
- Ruff

---

##  Project Structure

```text
ai-software-engineering-agent/
│
├── app/
│   │
│   ├── agents/
│   │   ├── planner.py
│   │   ├── coder.py
│   │   ├── tester.py
│   │   └── evaluator.py
│   │
│   ├── api/
│   │   └── routes/
│   │       ├── health.py
│   │       └── planner.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── graph/
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── llm/
│   │   ├── providers/
│   │   │   ├── mock_provider.py
│   │   │   └── openai_provider.py
│   │   │
│   │   ├── base.py
│   │   └── factory.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_health.py
│   ├── test_llm.py
│   ├── test_planner.py
│   ├── test_coder.py
│   ├── test_tester.py
│   ├── test_evaluator.py
│   └── test_workflow.py
│
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

---

##  Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/saba0-data/ai-software-engineering-agent.git
```

```bash
cd ai-software-engineering-agent
```

---

### 2️ Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

### 3️ Install Dependencies

```bash
pip install -e ".[dev]"
```

Or install the required packages manually:

```bash
pip install fastapi uvicorn langgraph pytest pytest-asyncio ruff
```

---

##  Environment Configuration

Create a `.env` file:

```bash
cp .env.example .env
```

Example configuration:

```env
LLM_PROVIDER=mock
OPENAI_API_KEY=your_api_key_here
```

The project supports a mock LLM provider for development and testing.

---

##  Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

##  API Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API directly from your browser.

---

##  API Endpoints

### Health Check

```http
GET /api/v1/health
```

Example response:

```json
{
  "status": "healthy"
}
```

---

### Create Software Development Plan

```http
POST /api/v1/plan
```

Example request:

```json
{
  "requirement": "Build a REST API for managing tasks with user authentication and CRUD operations."
}
```

Example response:

```json
{
  "requirement": "Build a REST API for managing tasks with user authentication and CRUD operations.",
  "plan": [
    "Analyze the software requirements",
    "Design the application architecture",
    "Implement data models and validation",
    "Implement API endpoints",
    "Write automated tests"
  ],
  "files": [
    "app/main.py",
    "app/models.py",
    "app/api/routes.py",
    "tests/test_api.py"
  ],
  "generated_code": {},
  "errors": []
}
```

---

##  Workflow Execution

The multi-agent workflow processes a software requirement through multiple stages.

```text
Requirement
    │
    ▼
Planner Agent
    │
    ▼
Coder Agent
    │
    ▼
Tester Agent
    │
    ▼
Evaluator Agent
    │
    ▼
Final Result
```

Each agent receives the shared workflow state and contributes its output to the next stage.

---

##  Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_planner.py -v
```

Example output:

```text
======================== test session starts ========================

tests/test_health.py .
tests/test_llm.py .
tests/test_planner.py .
tests/test_coder.py .
tests/test_tester.py .
tests/test_evaluator.py .
tests/test_workflow.py .

========================= passed =========================
```

---

##  Code Quality

Run Ruff:

```bash
ruff check .
```

Automatically fix supported issues:

```bash
ruff check . --fix
```

---

##  LLM Provider Architecture

The application uses an abstraction layer for LLM providers.

```text
                ┌───────────────────┐
                │   Agent Layer     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │  LLM Interface    │
                └─────────┬─────────┘
                          │
                ┌─────────┴─────────┐
                ▼                   ▼
       ┌────────────────┐   ┌────────────────┐
       │ Mock Provider  │   │ OpenAI Provider│
       └────────────────┘   └────────────────┘
```

This design makes it easier to switch LLM providers without modifying agent logic.

---

##  Key Engineering Concepts Demonstrated

This project demonstrates:

- Multi-agent system architecture
- Agent workflow orchestration
- State management
- REST API development
- Asynchronous Python programming
- LLM provider abstraction
- API design
- Automated testing
- Dependency management
- Code quality tooling
- Modular software architecture

---

##  Future Improvements

Potential improvements include:

-  Automatic retry workflows
-  More advanced agent reasoning
-  Workflow monitoring and observability
-  Persistent workflow storage
-  Docker containerization
-  Cloud deployment
-  Authentication and authorization
-  Agent performance metrics
-  Human-in-the-loop approval
-  Support for additional LLM providers

---

##  Author

**Saba Sulthana**

Aspiring Software Engineer | Python | AI | Data Science

🔗 GitHub: https://github.com/saba0-data

---

##  Why This Project?

This project was built to demonstrate how modern AI agents can automate parts of the software engineering lifecycle.

Instead of relying on a single LLM prompt, the system separates responsibilities between specialized agents and orchestrates them through a structured workflow.

The architecture focuses on:

- Separation of concerns
- Modular design
- Testability
- Extensibility
- API-first development
- Multi-agent orchestration

---

⭐ If you found this project interesting, consider starring the repository!
