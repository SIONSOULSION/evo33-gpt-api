from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def codex_bridge():
    return {"message": "Codex Bridge engine active."}