from fastapi import FastAPI as fastapi, APIRouter, FastAPI
from fastapi import APIRouter
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
router = APIRouter()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],)

@app.get("/")
def checker():
    return "BACKEND IS WORKING FINE"