from typing import TypedDict, Optional, List, Dict, Any


class MemoryItem(TypedDict):
    category: str          # preference | complaint | behavior | language
    content: str
    score: float


class OrderItem(TypedDict):
    order_id: str
    product_name: str
    status: str
    size: Optional[str]
    fit: Optional[str]


class TicketItem(TypedDict):
    ticket_id: str
    issue_type: str
    status: str
    resolution: Optional[str]


class InventoryItem(TypedDict):
    product_name: str
    size: str
    fit: str
    stock: int


class SupportState(TypedDict):
    # --- Identity ---
    user_anon_id: str

    # --- Input ---
    query: str

    # --- Routing ---
    intent: Optional[str]

    # --- Context ---
    memories: Optional[List[MemoryItem]]
    orders: Optional[List[OrderItem]]
    tickets: Optional[List[TicketItem]]
    inventory: Optional[List[InventoryItem]]

    # --- Output ---
    response: Optional[str]

    # --- Meta ---
    debug: Optional[Dict[str, Any]]
