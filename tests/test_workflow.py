import pytest

from app.graph.workflow import create_workflow


@pytest.mark.asyncio
async def test_workflow_runs() -> None:
    workflow = create_workflow()

    initial_state = {
        "requirement": "Build a REST API for managing tasks.",
        "plan": [],
        "files": [],
        "generated_code": {},
        "test_cases": [],
        "errors": [],
    }

    result = await workflow.ainvoke(initial_state)

    assert len(result["plan"]) > 0
    assert len(result["files"]) > 0
    assert len(result["generated_code"]) > 0
    assert "app/models.py" in result["generated_code"]

    assert len(result["test_cases"]) > 0
    assert "test_task_model_creation" in result["test_cases"]