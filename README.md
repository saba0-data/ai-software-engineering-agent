AI Software Engineering Agent Platform

A production-style multi-agent platform for automating software engineering workflows using Python, LangGraph, FastAPI, and LLMs.

The platform accepts a software requirement and orchestrates specialized AI agents to create a development plan, generate code, create test cases, and evaluate the implementation.

Features

Multi-agent workflow orchestration using LangGraph

Planner Agent for requirement analysis and software planning

Coder Agent for generating application code

Tester Agent for generating test cases

Evaluator Agent for evaluating generated implementations

LLM provider abstraction

Mock and OpenAI LLM providers

FastAPI REST API

Interactive Swagger documentation

Shared agent state management

Async agent execution

Automated testing with Pytest

Code quality checks with Ruff

Modular and extensible architecture

Environment-based configuration

Architecture

                         USER REQUIREMENT
                                |
                                v
                    +-----------------------+
                    |    PLANNER AGENT      |
                    |                       |
                    | Analyze requirements  |
                    | Create development    |
                    | plan and file list    |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    |     CODER AGENT       |
                    |                       |
                    | Generate application  |
                    | code for planned      |
                    | files                 |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    |    TESTER AGENT       |
                    |                       |
                    | Analyze generated     |
                    | code and generate     |
                    | test cases            |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    |   EVALUATOR AGENT     |
                    |                       |
                    | Evaluate generated    |
                    | implementation and    |
                    | return PASS / FAIL    |
                    +-----------+-----------+
                                |
                                v
                           FINAL RESULT

Technology Stack

Technology

Purpose

Python

Core application development

LangGraph

Multi-agent workflow orchestration

FastAPI

REST API framework

LLMs

AI-powered planning and code generation

Pydantic

Request and response validation

Pytest

Automated testing

Ruff

Code quality and linting

Uvicorn

ASGI application server

LangSmith

Agent tracing and observability support

Project Structure

ai-software-engineering-agent/
|
+-- app/
|   |
|   +-- agents/
|   |   +-- __init__.py
|   |   +-- planner.py
|   |   +-- coder.py
|   |   +-- tester.py
|   |   +-- evaluator.py
|   |
|   +-- api/
|   |   +-- routes/
|   |       +-- __init__.py
|   |       +-- health.py
|   |       +-- planner.py
|   |
|   +-- core/
|   |   +-- __init__.py
|   |   +-- config.py
|   |   +-- logging.py
|   |
|   +-- graph/
|   |   +-- __init__.py
|   |   +-- state.py
|   |   +-- workflow.py
|   |
|   +-- llm/
|   |   +-- __init__.py
|   |   +-- base.py
|   |   +-- factory.py
|   |   +-- providers/
|   |       +-- __init__.py
|   |       +-- mock_provider.py
|   |       +-- openai_provider.py
|   |
|   +-- main.py
|
+-- tests/
|   +-- __init__.py
|   +-- test_health.py
|   +-- test_llm.py
|   +-- test_planner.py
|   +-- test_planner_api.py
|   +-- test_coder.py
|   +-- test_tester.py
|   +-- test_evaluator.py
|   +-- test_state.py
|   +-- test_workflow.py
|
+-- .env.example
+-- .gitignore
+-- pyproject.toml
+-- README.md

Multi-Agent Workflow

The application uses specialized AI agents that communicate through a shared workflow state.

1. Planner Agent

The Planner Agent receives a software requirement and creates a structured software development plan.

Responsibilities

Analyze software requirements

Break requirements into implementation tasks

Identify required application files

Create a development strategy

Example Input

Build a REST API for managing tasks with user authentication and CRUD operations.

Example Output

{
  "plan": [
    "Analyze the software requirements",
    "Design the application architecture",
    "Define data models and validation",
    "Implement the API endpoints",
    "Write automated tests"
  ],
  "files": [
    "app/main.py",
    "app/models.py",
    "app/api/routes.py",
    "tests/test_api.py"
  ]
}

2. Coder Agent

The Coder Agent receives the software requirement, development plan, and identified files.

Responsibilities

Generate Python application code

Generate code for planned files

Follow the software development plan

Return structured generated code

Example output:

{
  "generated_code": {
    "app/main.py": "Generated Python code",
    "app/models.py": "Generated model code"
  }
}

3. Tester Agent

The Tester Agent analyzes the generated implementation and creates test scenarios.

Responsibilities

Analyze generated code

Generate test cases

Identify validation scenarios

Support automated software testing workflows

Example output:

{
  "test_cases": [
    "test_task_model_creation",
    "test_create_task",
    "test_get_task",
    "test_update_task",
    "test_delete_task"
  ]
}

4. Evaluator Agent

The Evaluator Agent evaluates the generated implementation.

Responsibilities

Review generated code

Review generated test cases

Evaluate implementation output

Return PASS or FAIL status

Example output:

{
  "evaluation": "PASS"
}

Agent State

The agents communicate through a shared state object.

{
    "requirement": "",
    "plan": [],
    "files": [],
    "generated_code": {},
    "test_cases": [],
    "evaluation": "",
    "retry_count": 0,
    "errors": []
}

This allows each agent to access the output of previous agents and contribute to the overall software engineering workflow.

LLM Provider Architecture

The application uses a provider abstraction layer to avoid tightly coupling agent logic to a specific LLM provider.

                 +------------------+
                 |   Application    |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 |   LLM Factory    |
                 +--------+---------+
                          |
              +-----------+-----------+
              |                       |
              v                       v
     +-----------------+     +-----------------+
     |  Mock Provider  |     | OpenAI Provider |
     +-----------------+     +-----------------+

The provider abstraction allows new LLM providers to be added without changing the core agent logic.

Supported providers include:

Mock Provider

OpenAI Provider

API

The application exposes REST APIs using FastAPI.

Health Check

GET /api/v1/health

Example response:

{
  "status": "healthy"
}

Create Software Development Plan

POST /api/v1/plan

Request:

{
  "requirement": "Build a REST API for managing tasks with user authentication and CRUD operations."
}

Example response:

{
  "requirement": "Build a REST API for managing tasks with user authentication and CRUD operations.",
  "plan": [
    "Analyze the software requirements",
    "Design the application architecture",
    "Define data models and validation",
    "Implement the API endpoints",
    "Write automated tests"
  ],
  "files": [
    "app/main.py",
    "app/models.py",
    "app/api/routes.py",
    "tests/test_api.py"
  ],
  "errors": []
}

API Documentation

FastAPI provides interactive Swagger documentation.

After starting the application, open:

http://127.0.0.1:8000/docs

Swagger UI can be used to:

Test API endpoints

Send software requirements

Inspect request schemas

Inspect response schemas

View workflow results

Installation

1. Clone the Repository

git clone https://github.com/saba0-data/ai-software-engineering-agent.git
cd ai-software-engineering-agent

2. Create a Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate

Linux/macOS

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install -e .

Install development dependencies:

pip install pytest pytest-asyncio httpx ruff

4. Configure Environment Variables

Copy the example environment file:

copy .env.example .env

Example configuration:

LLM_PROVIDER=mock
OPENAI_API_KEY=your_api_key

Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload

The application will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

Running Tests

Run all tests:

pytest

Run tests with verbose output:

pytest -v

The project includes tests for:

Health API

LLM provider abstraction

Planner Agent

Planner API

Coder Agent

Tester Agent

Evaluator Agent

Agent State

LangGraph workflow

Code Quality

Run Ruff:

ruff check .

Automatically fix supported issues:

ruff check . --fix

Key Engineering Concepts Demonstrated

AI Engineering

LLM integration

Prompt engineering

Multi-agent architecture

Agent orchestration

Context passing

Structured LLM output

AI evaluation

Backend Engineering

Python

FastAPI

REST APIs

Async programming

Pydantic validation

Modular architecture

Agent Orchestration

LangGraph workflows

Shared agent state

Sequential agent execution

State management

Retry tracking

Error handling

Software Engineering

Automated testing

Pytest

Code linting

Ruff

Environment configuration

Version control

Modular project design

Platform Architecture

LLM provider abstraction

Platform-agnostic architecture

Extensible provider design

Reusable agent components

Future Improvements

Human-in-the-loop approval workflows

Tool and function calling

RAG-based codebase context

GitHub repository integration

Automated code execution sandbox

Retry and agent recovery strategies

Agent observability dashboards

LangSmith tracing integration

Docker containerization

CI/CD with GitHub Actions

Authentication and access control

Agent evaluation datasets

Additional LLM providers

Why This Project

Modern software engineering teams are increasingly using AI systems to assist with:

Requirement analysis

Software planning

Code generation

Testing

Code evaluation

Development workflow automation

Instead of using a single chatbot, this project separates software engineering responsibilities into specialized AI agents.

Each agent performs a specific responsibility and communicates through a shared workflow state orchestrated using LangGraph.

This architecture demonstrates how AI agents can be integrated into structured software engineering workflows while maintaining modularity, extensibility, and platform flexibility.

Author

Saba Sulthana

GitHub: https://github.com/saba0-data

Project Repository: https://github.com/saba0-data/ai-software-engineering-agent

License

This project is created for educational and portfolio purposes.
