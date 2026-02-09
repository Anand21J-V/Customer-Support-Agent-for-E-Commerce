import os
from supabase import create_client
from dotenv import load_dotenv

# Explicitly load .env
load_dotenv(override=True)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase credentials not found in environment variables")

def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)
