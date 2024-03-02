from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from db import get_db
from models import Course, Enrollment
from schemas import CourseSchema, CourseGetSchema

router = APIRouter()


@router.get("/", response_model=list[CourseGetSchema])
async def read_all_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses


@router.get("/most-enrolled")
async def get_most_enrolled_course(db: Session = Depends(get_db)):
    most_enrolled_course = (
        db.query(Enrollment, func.count(Enrollment.courseID).label("count"))
        .group_by(Enrollment.courseID)
        .order_by(desc("count"))
        .first()
    )

    return {
        "courseID": most_enrolled_course[0].courseID,
        "courseName": most_enrolled_course[0].course.courseName,
        "credits": most_enrolled_course[0].course.credits,
        "count": most_enrolled_course[1],
    }


@router.get("/{course_id}", response_model=CourseGetSchema)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).get(course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.post("/", response_model=CourseGetSchema)
async def create_course(course: CourseSchema, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.delete("/{course_id}", response_model=CourseGetSchema)
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).get(course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(db_course)
    db.commit()
    return db_course


@router.get("/{course_id}/students")
async def get_course_students(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).get(course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return db_course.enrollments


@router.get("/highest-marks/{course_id}", response_model=int)
async def get_most_enrolled_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).get(course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    highest_marks = (
        db.query(Enrollment, func.max(Enrollment.marks))
        .filter(Enrollment.courseID == course_id)
        .first()
    )

    return highest_marks[1]
