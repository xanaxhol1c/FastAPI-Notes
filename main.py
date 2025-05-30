from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from todo.routes import router

app = FastAPI()

app.mount('/static', StaticFiles(directory='todo/static'), name='static')

app.include_router(router)