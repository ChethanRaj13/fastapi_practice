from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "sname" : "raj",
        "cgpa": 9.72,
        "test" : 40
    }
}

class Student(BaseModel):
    sname : str
    cgpa : float
    test : int

class UpdateStudent(BaseModel):
    sname: Optional[str] = None
    cgpa: Optional[float] = None
    test: Optional[int] = None


# first app
@app.get('/')
def index():
    return {"name":"first name"}

# path parameter
@app.get("/get-student/{student_id}")
def student_detail(student_id : int = Path(description="give Student ID", gt=0, lt=3)):
    return students[student_id]

# query parameter
@app.get("/get-by-name")
def get_by_name(*, name : Optional[str] = None, test : int):
    for id in students:
        if students[id]["sname"] == name:
            return students[id]
        return {"Data" : "Not Found"}

# post method
@app.post("/create-student/{student_id}")
def new_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "student already exists"}
    
    students[student_id] = student
    return students[student_id]

# put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student not found"}

    if student.sname is not None:
        students[student_id].sname = student.sname

    if student.cgpa is not None:
        students[student_id].cgpa = student.cgpa

    if student.test is not None:
        students[student_id].test = student.test

    return students[student_id]

@app .delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "student doesn't exist"}

    del students[student_id]
    return {"message" : "deleted successful"}

