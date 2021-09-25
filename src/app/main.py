import inspect

from fastapi import FastAPI
from fastapi.routing import APIRouter

from app import cases

app = FastAPI()


@app.get("/")
def home():
    return "Hello world"


def autodiscover(app: FastAPI):
    for _, module in inspect.getmembers(cases):
        for _, obj in inspect.getmembers(module):
            if isinstance(obj, APIRouter):
                app.include_router(obj)


autodiscover(app)
