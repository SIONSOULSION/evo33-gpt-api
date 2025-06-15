from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def inference_engine():
    return {"message": "Evo33 inference engine active."}