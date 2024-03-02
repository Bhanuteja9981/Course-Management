from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment
from db import get_db
from schemas import StudentSchema, StudentGetSchema


router = APIRouter()


@router.get("/", response_model=list[StudentGetSchema])
async def read_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


@router.get("/{student_id}", response_model=StudentGetSchema)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).get(student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.post("/", response_model=StudentGetSchema)
async def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.delete("/{student_id}", response_model=StudentGetSchema)
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).get(student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return db_student


@router.get("/{student_id}/courses")
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).get(student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return db_student.enrollments
