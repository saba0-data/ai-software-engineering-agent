from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.workflow import create_workflow


router = APIRouter()


class PlanRequest(BaseModel):
    requirement: str


class PlanResponse(BaseModel):
    requirement: str
    plan: list[str]
    files: list[str]
    generated_code: dict[str, str]
    test_cases: list[str]
    errors: list[str]


@router.post("/plan", response_model=PlanResponse)
async def create_plan(request: PlanRequest) -> PlanResponse:
    """Create a software development plan, code, and test cases."""

    workflow = create_workflow()

    initial_state = {
        "requirement": request.requirement,
        "plan": [],
        "files": [],
        "generated_code": {},
        "test_cases": [],
        "errors": [],
    }

    result = await workflow.ainvoke(initial_state)

    return PlanResponse(
        requirement=result["requirement"],
        plan=result["plan"],
        files=result["files"],
        generated_code=result["generated_code"],
        test_cases=result["test_cases"],
        errors=result["errors"],
    )