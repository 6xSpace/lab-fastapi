from fastapi import APIRouter
from .schema import StudentCreateSchema, StudentUpdateSchema

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/")
async def create_item(item: StudentCreateSchema):
    studentsTab.append(item)
    return item

@router.patch("/{item_id}")
async def update_item(item_id: int, item: StudentUpdateSchema):
    # results = {"item_id": item_id, "item": item}
    if item_id < len(studentsTab):

        studentsTab[item_id] = item

        return item
    else:
        return "nie ma :("