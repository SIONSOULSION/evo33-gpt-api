# Placeholder for /explain route
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def explain_logic():
    return {"message": "Explanation endpoint active"}

