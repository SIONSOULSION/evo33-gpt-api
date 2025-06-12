from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def scroll():
    return {"message": "Scroll endpoint"}
