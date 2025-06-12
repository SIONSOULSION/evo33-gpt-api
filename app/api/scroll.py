from fastapi import APIRouter

router = APIRouter()

@router.get("/scroll")
def scroll():
    return {"message": "Scroll endpoint"}
