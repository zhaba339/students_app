from fastapi import FastAPI, Query
from app.utils import json_to_dict_list
import os
from typing import Optional
from app.models import Student


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'app/students.json')


app = FastAPI()


@app.get("/")
def home():
    return {'message': 'Hello, World!'}


@app.get("/students")
def get_all_students():
    students = json_to_dict_list(path_to_json)
    return students


@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student['course'] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


@app.get("/student/{student_id}")
def get_student_on_student_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student['student_id'] == student_id:
            filtered_students.append(student)

    return filtered_students


@app.get("/student")
def get_student_on_student_id_params(student_id: int) -> Student:
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student['student_id'] == student_id:
            return student


@app.get("/register")
def register_user():
    return {"text": "Здесь будет форма регистрации"}

