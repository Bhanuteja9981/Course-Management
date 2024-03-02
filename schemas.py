from pydantic import BaseModel


class StudentSchema(BaseModel):
    firstName: str
    lastName: str
    email: str


class StudentGetSchema(StudentSchema):
    id: int


class CourseSchema(BaseModel):
    courseName: str
    credits: float


class CourseGetSchema(CourseSchema):
    id: int


class EnrollmentSchema(BaseModel):
    courseID: int
    studentID: int

class updateMarks(EnrollmentSchema):
    marks: int