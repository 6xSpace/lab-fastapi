from pydantic import BaseModel

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str|None
    last_name: str|None