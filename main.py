from fastapi import FastAPI
from db import Base, engine
import uvicorn
from routes import students, courses, enrollments

Base.metadata.create_all(engine)

app = FastAPI(root_path="/api", debug=True)

app.include_router(students.router, prefix="/students")
app.include_router(courses.router, prefix="/courses")
app.include_router(enrollments.router, prefix="/enrollments")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
