from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def schema():
    return {"message": "Schema endpoint"}
