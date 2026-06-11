from pydantic import BaseModel

class StudentCreate(BaseModel):
    reg_no: str
    name: str
    course: str


class StudentResponse(BaseModel):
    id: int
    reg_no: str
    name: str
    course: str

    class Config:
        from_attributes = True
