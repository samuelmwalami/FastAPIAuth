from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def add_task():
    return