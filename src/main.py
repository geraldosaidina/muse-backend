from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database.database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Message": "Hello, World"}