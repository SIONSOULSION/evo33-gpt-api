from fastapi import APIRouter

router = APIRouter()

@router.get("/solve-legacy")
def solve_legacy():
    return {"message": "Solve legacy endpoint"}
