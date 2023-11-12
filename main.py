from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

@app.get('/')
def hello_world():
  return "Hello world!"

models.Base.metadata.create_all(engine)
