import json

from app.graph.state import AgentState
from app.llm.factory import get_llm_provider

PLANNER_SYSTEM_PROMPT = """
You are a senior software engineer responsible for planning software projects.

Analyze the user's software requirement and create a development plan.

Return ONLY valid JSON in this format:

{
    "plan": [
        "step 1",
        "step 2"
    ],
    "files": [
        "path/to/file.py"
    ]
}
"""


async def planner_agent(state: AgentState) -> dict:
    """Create a software development plan from a requirement."""

    llm = get_llm_provider()

    response = await llm.generate(
        prompt=state["requirement"],
        system_prompt=PLANNER_SYSTEM_PROMPT,
    )

    try:
        result = json.loads(response)

        return {
            "plan": result.get("plan", []),
            "files": result.get("files", []),
        }

    except json.JSONDecodeError:
        return {
            "plan": [],
            "files": [],
            "errors": ["Planner returned invalid JSON."],
        }