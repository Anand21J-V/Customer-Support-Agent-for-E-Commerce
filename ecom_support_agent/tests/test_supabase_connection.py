from ecom_support_agent.app.db.supabase_client import get_supabase_client

def test_supabase_connection():
    supabase = get_supabase_client()

    response = supabase.table("inventory").select("*").limit(1).execute()

    assert response is not None
