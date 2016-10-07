import os
from database import db
from database import Employee, EmployeeLeave

def populateEmployeeTable():
    employee1 = Employee(name="John Carter", email="john.carter@anubhav83.in")
    employee2= Employee(name="Darth Vader", email="darth.vader@anubhav83.in")
    employee3= Employee(name="John Malkovich", email="john.alkovich@anubhav83.in")
    db.session.add(employee1)
    db.session.add(employee2)
    db.session.add(employee3)
    db.session.commit()

def populateEmployeeLeaveTable():
    john_carter = Employee.query.filter_by(name="John Carter").first()
    print john_carter
    darth_vader = Employee.query.filter_by(name="Darth Vader").first()
    john_malkovich = Employee.query.filter_by(name="John Malkovich").first()

    # Employee John Carter is on leave on the 10th day of the current month
    l1 = EmployeeLeave(employee_id=john_carter.id, leave_day=10)
    l2 = EmployeeLeave(employee_id=john_carter.id, leave_day=12)
    l3 = EmployeeLeave(employee_id=john_carter.id, leave_day=14)

    john_carter.leave.append(l1)
    john_carter.leave.append(l2)
    john_carter.leave.append(l3)
    db.session.add(john_carter)

    # Employee Darth Vader is on leave on the 10th day of the current month
    l1 = EmployeeLeave(employee_id=darth_vader.id, leave_day=3)
    l2 = EmployeeLeave(employee_id=darth_vader.id, leave_day=5)
    l3 = EmployeeLeave(employee_id=darth_vader.id, leave_day=11)
    l4 = EmployeeLeave(employee_id=darth_vader.id, leave_day=12)
    l5 = EmployeeLeave(employee_id=darth_vader.id, leave_day=13)
    l6 = EmployeeLeave(employee_id=darth_vader.id, leave_day=14)

    darth_vader.leave.append(l1)
    darth_vader.leave.append(l2)
    darth_vader.leave.append(l3)
    darth_vader.leave.append(l4)
    darth_vader.leave.append(l5)
    darth_vader.leave.append(l6)
    db.session.add(darth_vader)

    # Employee John Malkovich is on leave on the 10th day of the current month
    l1 = EmployeeLeave(employee_id=john_malkovich.id, leave_day=23)
    l2 = EmployeeLeave(employee_id=john_malkovich.id, leave_day=25)
    l3 = EmployeeLeave(employee_id=john_malkovich.id, leave_day=27)

    john_malkovich.leave.append(l1)
    john_malkovich.leave.append(l2)
    john_malkovich.leave.append(l3)
    db.session.add(john_malkovich)

    db.session.commit()

def init_db(database_path):
    if not os.path.exists(database_path):
        db.create_all()
        populateEmployeeTable()
        populateEmployeeLeaveTable()
