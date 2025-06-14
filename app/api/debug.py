# Placeholder for /debug route
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def debug_logic():
    return {"message": "Debug endpoint active"}

