import pytest

from app.agents.planner import planner_agent
from app.graph.state import AgentState


@pytest.mark.asyncio
async def test_planner_agent_creates_plan() -> None:
    state: AgentState = {
        "requirement": "Build a REST API for managing tasks.",
        "plan": [],
        "files": [],
        "generated_code": {},
        "test_cases": [],
        "errors": [],
    }

    result = await planner_agent(state)

    assert len(result["plan"]) > 0
    assert len(result["files"]) > 0