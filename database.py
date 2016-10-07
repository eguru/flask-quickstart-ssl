from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

from flask_admin.contrib import sqla


db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    leave = db.relationship('EmployeeLeave', backref="employees",
                            cascade="all, delete-orphan" , lazy='dynamic')

    def __unicode__(self):
        return self.name

class EmployeeAdmin(sqla.ModelView):
    form_columns = ['name', 'email', 'leave']

class EmployeeLeave(db.Model):
    __tablename__ = 'employee_leave'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    leave_day = Column(Integer)

    def __unicode__(self):
        return self.user_id

class EmployeeLeaveAdmin(sqla.ModelView):
    form_columns = ['employee_id', 'leave_day']
