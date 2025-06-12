from fastapi import APIRouter

router = APIRouter()

@router.get("/schema")
def schema():
    return {"message": "Schema endpoint"}
