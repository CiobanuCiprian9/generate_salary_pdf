from app import myapp
from extensions import db
from Models.EmployeeModel import Employee
from Models.BonusModel import Bonus
from Models.SalaryModel import Salary
from Models.AttendanceModel import Attendance

with myapp.app_context():
    db.create_all()
