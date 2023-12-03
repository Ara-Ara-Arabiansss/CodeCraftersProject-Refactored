from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify
from .decorators import staff_required

from App import db
from App.models import Department
import App.controllers.department as dept_controller

department_views = Blueprint('department_views', __name__, template_folder='../templates')

@department_views('/departments', methods=['GET'])
@staff_required
def get_departments():
    departments = Department.query.all()
    return jsonify({'departments': [department.name for department in departments]})

@department_views('/departments/<int:department_id>', methods=['GET'])
@staff_required
def get_department(department_id):
    department = Department.query.get_or_404(department_id)
    return jsonify({'department': department.name})

@department_views('/departments', methods=['POST'])
@staff_required
def create_department():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_department = Department(name=name)
    db.session.add(new_department)
    db.session.commit()

    return jsonify({'message': 'Department created successfully'}), 201

@department_views('/departments/<int:department_id>', methods=['PUT'])
@staff_required
def update_department(department_id):
    department = Department.query.get_or_404(department_id)
    data = request.get_json()
    new_name = data.get('name')

    if not new_name:
        return jsonify({'error': 'Name is required'}), 400

    department.name = new_name
    db.session.commit()

    return jsonify({'message': 'Department updated successfully'})

@department_views('/departments/<int:department_id>', methods=['DELETE'])
@staff_required
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()

    return jsonify({'message': 'Department deleted successfully'})
