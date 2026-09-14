import json

from app.graph.state import AgentState
from app.llm.factory import get_llm_provider


CODER_SYSTEM_PROMPT = """
You are a senior Python software engineer responsible for implementing software.

Use the software requirement, development plan, and suggested files
to generate implementation code.

Return ONLY valid JSON in this format:

{
    "generated_code": {
        "path/to/file.py": "Python source code"
    }
}
"""


async def coder_agent(state: AgentState) -> dict:
    """Generate implementation code from the software development plan."""

    llm = get_llm_provider()

    context = json.dumps(
        {
            "requirement": state["requirement"],
            "plan": state["plan"],
            "files": state["files"],
        }
    )

    response = await llm.generate(
        prompt=context,
        system_prompt=CODER_SYSTEM_PROMPT,
    )

    try:
        result = json.loads(response)

        return {
            "generated_code": result.get("generated_code", {}),
        }

    except json.JSONDecodeError:
        return {
            "generated_code": {},
            "errors": ["Coder returned invalid JSON."],
        }