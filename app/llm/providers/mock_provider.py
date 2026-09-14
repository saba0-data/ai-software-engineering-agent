import json

from app.llm.base import BaseLLMProvider


class MockLLMProvider(BaseLLMProvider):
    """Mock provider for local development and testing."""

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        system_prompt = system_prompt or ""

        if "planning software projects" in system_prompt:
            return json.dumps(
                {
                    "plan": [
                        "Analyze the software requirements",
                        "Design the application architecture",
                        "Define data models and validation",
                        "Implement the API endpoints",
                        "Write automated tests",
                    ],
                    "files": [
                        "app/main.py",
                        "app/models.py",
                        "app/api/routes.py",
                        "tests/test_api.py",
                    ],
                }
            )

        if "implementing software" in system_prompt:
            return json.dumps(
                {
                    "generated_code": {
                        "app/models.py": (
                            "from pydantic import BaseModel\n\n"
                            "class Task(BaseModel):\n"
                            "    title: str\n"
                            "    completed: bool = False\n"
                        ),
                        "app/api/routes.py": (
                            "from fastapi import APIRouter\n\n"
                            "router = APIRouter()\n\n"
                            "@router.get('/tasks')\n"
                            "async def get_tasks():\n"
                            "    return []\n"
                        ),
                    }
                }
            )

        if "testing software" in system_prompt:
            return json.dumps(
                {
                    "test_cases": [
                        "test_task_model_creation",
                        "test_get_tasks_endpoint",
                        "test_task_validation",
                    ]
                }
            )

        if (
            "evaluating generated software" in system_prompt
            or "software engineering reviewer" in system_prompt
            or "evaluating software" in system_prompt
        ):
            return json.dumps(
                {
                    "evaluation": "PASS",
                }
            )

        return json.dumps(
            {
                "errors": [
                    "Mock provider did not recognize the requested agent."
                ]
            }
        )