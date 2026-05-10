from langgraph.graph import (
    StateGraph,
    END,
)

from graph.nodes import (
    AgentState,
    call_model,
    call_tool,
)


def should_continue(state):

    last_message = state["messages"][-1]

    if getattr(
        last_message,
        "tool_calls",
        None
    ):
        return "tool"

    return END


workflow = StateGraph(AgentState)

workflow.add_node(
    "llm",
    call_model,
)

workflow.add_node(
    "tool",
    call_tool,
)

workflow.set_entry_point("llm")

workflow.add_conditional_edges(
    "llm",
    should_continue,
    {
        "tool": "tool",
        END: END,
    },
)

workflow.add_edge(
    "tool",
    "llm",
)

graph = workflow.compile()
