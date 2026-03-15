from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "sname" : "raj",
        "cgpa": 9.72,
        "test" : 40
    }
}

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