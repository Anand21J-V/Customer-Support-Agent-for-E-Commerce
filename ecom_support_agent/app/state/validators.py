from ecom_support_agent.app.state.support_state import SupportState


REQUIRED_FIELDS = ["user_anon_id", "query"]


def validate_state(state: SupportState) -> None:
    for field in REQUIRED_FIELDS:
        if field not in state or not state[field]:
            raise ValueError(f"Missing required state field: {field}")
