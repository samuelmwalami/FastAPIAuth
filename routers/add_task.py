from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/")
async def add_task():
    return