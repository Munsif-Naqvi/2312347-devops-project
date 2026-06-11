from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app import models, schemas


app = FastAPI()


REG_NO = "2312347"


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)



# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "db": "connected",
        "student": REG_NO
    }



# -------------------------
# CREATE STUDENT
# -------------------------



@app.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(
        reg_no=student.reg_no,
        name=student.name,
        course=student.course
    )


    db.add(new_student)
    db.commit()
    db.refresh(new_student)


    return new_student


# -------------------------
# GET ALL STUDENTS
# -------------------------


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


# -------------------------
# GET STUDENT BY REG_NO
# -------------------------


@app.get("/students/{reg_no}")
def get_student(reg_no: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.reg_no == reg_no).first()


    if not student:
        raise HTTPException(status_code=404, detail="Student not found")


    return student
