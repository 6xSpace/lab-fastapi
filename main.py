from fastapi import FastAPI
from pydantic import BaseModel
from functools import lru_cache

import students

app = FastAPI()



@app.get("/")
def root():
    return {"text": "HELLLO"}

app.include_router(students.router, prefix="/students")