from app.graph.state import AgentState


def test_agent_state_structure() -> None:
    state: AgentState = {
        "requirement": "Build a task management API",
        "plan": [],
        "files": [],
        "generated_code": {},
        "test_cases": [],
        "errors": [],
    }

    assert state["requirement"] == "Build a task management API"
    assert state["plan"] == []
    assert state["generated_code"] == {}
    assert state["test_cases"] == []