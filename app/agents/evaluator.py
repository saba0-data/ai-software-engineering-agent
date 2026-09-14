import json

from app.graph.state import AgentState
from app.llm.factory import get_llm_provider


EVALUATOR_SYSTEM_PROMPT = """
You are a senior software engineering reviewer responsible for
evaluating generated software.

Review the requirement, generated code, and test cases.

Determine whether the implementation meets the requirements.

Return ONLY valid JSON:

{
    "evaluation": "PASS"
}

or:

{
    "evaluation": "FAIL"
}
"""


async def evaluator_agent(state: AgentState) -> dict:
    """Evaluate generated software and test cases."""

    llm = get_llm_provider()

    context = json.dumps(
        {
            "requirement": state["requirement"],
            "generated_code": state["generated_code"],
            "test_cases": state["test_cases"],
        }
    )

    response = await llm.generate(
        prompt=context,
        system_prompt=EVALUATOR_SYSTEM_PROMPT,
    )

    try:
        result = json.loads(response)

        return {
            "evaluation": result.get("evaluation", "FAIL"),
        }

    except json.JSONDecodeError:
        return {
            "evaluation": "FAIL",
            "errors": ["Evaluator returned invalid JSON."],
        }