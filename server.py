import os
import sys
import calendar
import datetime
from flask import Flask
from flask import render_template
import flask_admin as admin
from database import db, Employee, EmployeeLeave
from database import db, EmployeeAdmin, EmployeeLeaveAdmin
from mock import db_mock

app_path = os.path.dirname(os.path.abspath(__file__))
if app_path not in sys.path:
    sys.path.append(app_path)

database_path = "%s/employee.db"%app_path

app = Flask(__name__)

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s'%database_path
app.config['SQLALCHEMY_ECHO'] = True
# init app this way would allow us to separate out model code into a separate
# file (database.py)
db.init_app(app)

#Create tables and initialize data
with app.app_context():
    db_mock.init_db(database_path)

# Create admin
admin = admin.Admin(app, name='Admin Quickstart', template_mode='bootstrap3')
admin.add_view(EmployeeAdmin(Employee, db.session))
admin.add_view(EmployeeLeaveAdmin(EmployeeLeave, db.session))

@app.route('/')
def index():
    now = datetime.datetime.now()
    month_days = calendar.monthrange(now.year, now.month)[1]
    employee_leave_data = {}
    for employee in Employee.query.all():
        employee_leave_data.setdefault(
                employee, [leave.leave_day for leave in employee.leave.all()])

    data = {'year' : now.year,
            'month': now.strftime("%B"),
            'day': now.day,
            'months' : calendar.month_name[1:],
            'month_days': range(1, month_days+1),
            'employee_leave_data': employee_leave_data}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    #app.run(debug=True, port=8080)
    app.run(debug=True, host='0.0.0.0', port=8080,
            ssl_context=('res/server.crt', 'res/server.key'))
