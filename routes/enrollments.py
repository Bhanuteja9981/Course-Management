from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Enrollment, Course, Student
from schemas import EnrollmentSchema, updateMarks

router = APIRouter()


@router.post("/enroll")
async def enroll(enroll: EnrollmentSchema, db: Session = Depends(get_db)):
    db_course = db.query(Course).get(enroll.courseID)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_student = db.query(Student).get(enroll.studentID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollment = Enrollment(course=db_course, student=db_student)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment


@router.delete("/unenroll")
async def unenroll(enroll: EnrollmentSchema, db: Session = Depends(get_db)):
    enrollment = (
        db.query(Enrollment)
        .filter_by(courseID=enroll.courseID, studentID=enroll.studentID)
        .first()
    )
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    db.delete(enrollment)
    db.commit()
    return enrollment


@router.put("/updateMarks")
async def read_all_courses(data: updateMarks, db: Session = Depends(get_db)):
    enrollment = (
        db.query(Enrollment)
        .filter_by(studentID=data.studentID, courseID=data.courseID)
        .first()
    )
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    # update marks
    enrollment.marks = data.marks
    db.commit()

    return enrollment
