from ecom_support_agent.app.state.support_state import SupportState


def create_initial_state(user_anon_id: str, query: str) -> SupportState:
    return {
        "user_anon_id": user_anon_id,
        "query": query,
        "intent": None,
        "memories": None,
        "orders": None,
        "tickets": None,
        "inventory": None,
        "response": None,
        "debug": {}
    }
