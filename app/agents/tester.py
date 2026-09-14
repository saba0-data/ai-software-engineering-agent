import json

from app.graph.state import AgentState
from app.llm.factory import get_llm_provider


TESTER_SYSTEM_PROMPT = """
You are a senior software engineer responsible for testing software.

Analyze the generated code and identify important test cases.

Return ONLY valid JSON in this format:

{
    "test_cases": [
        "test_case_name"
    ]
}
"""


async def tester_agent(state: AgentState) -> dict:
    """Generate test cases for the implementation."""

    llm = get_llm_provider()

    context = json.dumps(
        {
            "requirement": state["requirement"],
            "generated_code": state["generated_code"],
        }
    )

    response = await llm.generate(
        prompt=context,
        system_prompt=TESTER_SYSTEM_PROMPT,
    )

    try:
        result = json.loads(response)

        return {
            "test_cases": result.get("test_cases", []),
        }

    except json.JSONDecodeError:
        return {
            "test_cases": [],
            "errors": ["Tester returned invalid JSON."],
        }