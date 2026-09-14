from typing import TypedDict


class AgentState(TypedDict):
    """Shared state for the software engineering agent workflow."""

    requirement: str
    plan: list[str]
    files: list[str]
    generated_code: dict[str, str]
    test_cases: list[str]
    evaluation: str
    retry_count: int
    errors: list[str]