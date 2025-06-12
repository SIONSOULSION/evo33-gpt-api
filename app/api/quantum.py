from fastapi import APIRouter

router = APIRouter()

@router.get("/quantum")
def quantum():
    return {"message": "Quantum endpoint"}
