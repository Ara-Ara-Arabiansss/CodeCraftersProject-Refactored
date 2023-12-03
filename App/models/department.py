from App.database import db

class Department(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    courses_list = db.relationship('Course', back_populates='department')
    courses = db.relationship('Course', back_populates='department', overlaps="courses_list")  # Add overlaps parameter
    programs = db.relationship('Program', back_populates='department')

    def __init__(self, name):
        self.name = name
        
