from App.models import Student, CoursePlan, Program
from App.controllers import (get_program_by_name)
from App.database import db

def create_student(student_id, password, name, programname):
    try:
        program = get_program_by_name(programname)
        if program:
            student = Student.query.filter_by(id=student_id, name=name, program_id=program.id).first()
            if student is not None:
                print("Student exists already")
                return None
            else:
                new_student = Student(student_id, password, name, program.id)
                db.session.add(new_student)
                db.session.commit()
                print("Student successfully created")
                return new_student
        else:
            print("Program doesn't exist")
    except Exception as e:
        db.session.rollback()
        print(f'Error creating student: {e}')

def get_student_by_id(ID):
    return Student.query.filter_by(id=ID).first()

def get_student(id):
    return Student.query.get(id)

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students_json = [student.get_json() for student in students]
    return students_json

def update_student(id, username):
    student = get_student_by_id(id)
    if student:
        student.name = username
        db.session.add(student)
        db.session.commit()
        return student

def enroll_in_programme(student_id, programme_id):
    student = get_student_by_id(student_id)
    if student:
        programme = Program.query.get(programme_id)
        if programme:
            student.program_id = programme_id
            db.session.add(student)
            db.session.commit()
    return student.program_id

def verify_student(username):
    student=Student.query.filter_by(id=username).first()
    if student:
        return True
    return False


