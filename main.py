from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/student")
async def create_item(item: StudentCreateSchema):
    return item

