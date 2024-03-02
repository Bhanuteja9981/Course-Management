from sqlalchemy import Column, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from db import Base


# Database model parameters
# Student: [ Long: studentID, String: firstName, String: lastName, String: email, List<Enrollment>: enrollments ]
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, index=True)
    lastName = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    enrollments = relationship("Enrollment", back_populates="student")


# Course: [ Long: course, String: courseName, double: credits, List<Enrollment>: enrollments ]
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    courseName = Column(String, index=True)
    credits = Column(Float)

    enrollments = relationship("Enrollment", back_populates="course")


# Enrollment: [Student: student, Course: course, int: marks ]
class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    studentID = Column(Integer, ForeignKey("students.id"))
    courseID = Column(Integer, ForeignKey("courses.id"))
    marks = Column(Integer)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    __table_args__ = (UniqueConstraint("studentID", "courseID"),)
