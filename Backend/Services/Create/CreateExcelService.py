from sqlalchemy import extract
import pandas as pd
from Models.EmployeeModel import Employee
from Models.SalaryModel import Salary
from Models.AttendanceModel import Attendance
from Models.BonusModel import Bonus
from datetime import date
from Services.Calculate.CalculateSalaryService import calculateSalary
from Services.Calculate.CalculateBonusService import calculateBonus
import os

EXCEL_FOLDER = "reports/excel_reports"
os.makedirs(EXCEL_FOLDER, exist_ok=True)

def createExcel():
    managers = Employee.query.filter(Employee.id_employee.like("M%")).all()

    for mgr in managers:
        subordinates = Employee.query.filter_by(id_manager=mgr.id_employee).all()

        today = date.today()
        year, month = today.year, today.month

        data = []
        employees = Employee.query.all()

        for emp in subordinates:
            id_emp = emp.id_employee

            salary = Salary.query.filter_by(id_employee=id_emp).first()

            attendance = Attendance.query.filter_by(id_employee=id_emp).filter(
                extract('month', Attendance.month) == month,
                extract('year', Attendance.month) == year
            ).first()

            bonus = Bonus.query.filter_by(id_employee=id_emp).first()


            data.append({
                "Name": f"{emp.first_name} {emp.last_name}",
                "Salary to be paid(without bonus)": calculateSalary(salary.base_salary,attendance.hours_worked // 8) if salary else 0,
                "Working Days": attendance.hours_worked // 8 if attendance else 0,
                "Vacation Days": attendance.day_vacation if attendance else 0,
                "Bonuses": calculateBonus(salary.base_salary,attendance, bonus) if salary and attendance and bonus else 0
            })

        df = pd.DataFrame(data)
        df.to_excel(os.path.join(EXCEL_FOLDER, f"manager_{mgr.id_employee}.xlsx"), index=False)