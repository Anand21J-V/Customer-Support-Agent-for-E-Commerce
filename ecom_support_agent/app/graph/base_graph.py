from langgraph.graph import StateGraph, END
from ecom_support_agent.app.state.support_state import SupportState
from ecom_support_agent.app.llm.groq_client import call_llm


def dummy_node(state: SupportState) -> SupportState:
    user_query = state["query"]

    messages = [
        {"role": "system", "content": "You are a test assistant."},
        {"role": "user", "content": user_query}
    ]

    response = call_llm(messages)

    return {
        "query": user_query,
        "response": response
    }


def build_graph():
    graph = StateGraph(SupportState)

    graph.add_node("dummy", dummy_node)
    graph.set_entry_point("dummy")
    graph.add_edge("dummy", END)

    return graph.compile()
