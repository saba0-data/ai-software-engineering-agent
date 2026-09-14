from langgraph.graph import END, START, StateGraph

from app.agents.coder import coder_agent
from app.agents.planner import planner_agent
from app.agents.tester import tester_agent
from app.graph.state import AgentState


def create_workflow():
    """Create the software engineering agent workflow."""

    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_agent)
    workflow.add_node("coder", coder_agent)
    workflow.add_node("tester", tester_agent)

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "coder")
    workflow.add_edge("coder", "tester")
    workflow.add_edge("tester", END)

    return workflow.compile()