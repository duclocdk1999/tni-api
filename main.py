from app.config import STATIC_DIR
from app.images.router import router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(router)