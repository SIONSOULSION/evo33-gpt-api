from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def quantum():
    return {"message": "Quantum endpoint"}
