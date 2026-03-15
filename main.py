from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name" : "raj",
        "cgpa": 9.72
    }
}

@app.get('/')
def index():
    return {"name":"first name"}

@app.get("/get-student/{student_id}")
def student_detail(student_id : int = Path(description="give Student ID", gt=0, lt=3)):
    return students[student_id]