import json
from ecom_support_agent.app.llm.groq_client import call_llm
from ecom_support_agent.app.state.support_state import SupportState
from ecom_support_agent.app.agents.intent_router.prompt import (
    INTENT_ROUTER_SYSTEM_PROMPT
)

ALLOWED_INTENTS = {
    "order_status",
    "refund",
    "recommendation",
    "complaint",
    "general"
}


def intent_router_agent(state: SupportState) -> SupportState:
    user_query = state["query"]

    messages = [
        {"role": "system", "content": INTENT_ROUTER_SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]

    raw_output = call_llm(messages, temperature=0.0)

    try:
        parsed = json.loads(raw_output)
        intent = parsed.get("intent")

        if intent not in ALLOWED_INTENTS:
            raise ValueError("Invalid intent returned by model")

    except Exception:
        intent = "general"  # safe fallback

    return {
        **state,
        "intent": intent
    }
