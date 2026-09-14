import pytest

from app.agents.coder import coder_agent
from app.graph.state import AgentState


@pytest.mark.asyncio
async def test_coder_agent_generates_code() -> None:
    state: AgentState = {
        "requirement": "Build a REST API for managing tasks.",
        "plan": [
            "Analyze the software requirements",
            "Design the application architecture",
            "Implement the API endpoints",
        ],
        "files": [
            "app/models.py",
            "app/api/routes.py",
        ],
        "generated_code": {},
        "test_cases": [],
        "errors": [],
    }

    result = await coder_agent(state)

    assert len(result["generated_code"]) > 0
    assert "app/models.py" in result["generated_code"]