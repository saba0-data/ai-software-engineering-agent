import pytest

from app.agents.evaluator import evaluator_agent as run_evaluator_agent
from app.graph.state import AgentState


@pytest.mark.asyncio
async def test_evaluator_agent_returns_pass() -> None:
    state: AgentState = {
        "requirement": "Build a REST API for managing tasks.",
        "plan": [],
        "files": [],
        "generated_code": {
            "app/models.py": "class Task: pass",
        },
        "test_cases": [
            "test_task_model_creation",
        ],
        "evaluation": "",
        "retry_count": 0,
        "errors": [],
    }

    result = await run_evaluator_agent(state)

    assert result["evaluation"] == "PASS"