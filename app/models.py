from sqlalchemy import Column, Integer, String
from app.database import Base


class Student(Base):


    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    reg_no = Column(String, unique=True, index=True)
    name = Column(String)
    course = Column(String)
