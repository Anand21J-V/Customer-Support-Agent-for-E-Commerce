import pytest
from ecom_support_agent.app.state.state_factory import create_initial_state
from ecom_support_agent.app.state.validators import validate_state


def test_initial_state_valid():
    state = create_initial_state(
        user_anon_id="user_123",
        query="Where is my order?"
    )
    validate_state(state)


def test_missing_user_id_fails():
    with pytest.raises(ValueError):
        validate_state({
            "query": "Test"
        })
