# Support agent state (empty for now)
from typing import TypedDict

class SupportState(TypedDict):
    query: str
    response: str
