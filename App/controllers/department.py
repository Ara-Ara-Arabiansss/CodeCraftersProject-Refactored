from App import db
from App.models import Department
from App.models import Program
from App.controllers.program import get_program_by_id

# Create new department
def create_department(name, building):
    dept = Department(name=name, building=building)
    db.session.add(dept)
    db.session.commit()
    return dept

# Get single department by id/name
def get_department(id):
    return Department.query.get(id) 

def get_department_by_name(name):
    return Department.query.filter_by(name=name).first()

# List all departments   
def get_all_departments():
    return Department.query.all()

# Add program to a department
def add_program_to_department(program_id, dept_name):
    program = get_program_by_id(program_id)
    dept = get_department_by_name(dept_name)  
    if program and dept:
        dept.programs.append(program)
        db.session.commit()
    return program