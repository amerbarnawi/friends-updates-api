from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()


@app.get("/")
def hw():
    return "Hello world"


models.Base.metadata.create_all(engine)
