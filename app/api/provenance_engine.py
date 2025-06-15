from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def provenance():
    return {"message": "Provenance engine active."}