from fastapi import FastAPI
from .routers import router

app = FastAPI(title="Renewable Energy Management API")
app.include_router(router)
