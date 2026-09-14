import pytest

from app.agents.tester import tester_agent as run_tester_agent
from app.graph.state import AgentState


@pytest.mark.asyncio
async def test_tester_agent_generates_test_cases() -> None:
    state: AgentState = {
        "requirement": "Build a REST API for managing tasks.",
        "plan": [],
        "files": [],
        "generated_code": {
            "app/models.py": "class Task: pass",
        },
        "test_cases": [],
        "errors": [],
    }

    result = await run_tester_agent(state)

    assert len(result["test_cases"]) > 0
    assert "test_task_model_creation" in result["test_cases"]