from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def home() -> dict:
    pass