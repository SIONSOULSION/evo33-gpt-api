from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def solve_legacy():
    return {"message": "Solve legacy endpoint"}
    