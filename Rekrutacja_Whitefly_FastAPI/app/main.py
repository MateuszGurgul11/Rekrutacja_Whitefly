from fastapi import FastAPI
from app.views import router as view_router
from app.database import database

app = FastAPI()

app.include_router(view_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
