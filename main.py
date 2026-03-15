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
