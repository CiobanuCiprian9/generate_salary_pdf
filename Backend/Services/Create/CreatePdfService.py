from Models.EmployeeModel import Employee
from Models.SalaryModel import Salary
from Models.AttendanceModel import Attendance
from Models.BonusModel import Bonus
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os
import calendar

from Services.Calculate.CalculateSalaryService import calculateSalary
from Services.Calculate.CalculateBonusService import calculateBonus

PDF_FOLDER = "reports/pdf_payslip"
os.makedirs(PDF_FOLDER, exist_ok=True)

def createPdf():
    employees = Employee.query.all()
    today = date.today()
    luna_text = calendar.month_name[today.month]
    anul = today.year

    for emp in employees:
        salary = Salary.query.filter_by(id_employee=emp.id_employee).first()
        bonus = Bonus.query.filter_by(id_employee=emp.id_employee).first()
        attendance = Attendance.query.filter_by(id_employee=emp.id_employee).first()

        if not salary or not attendance:
            continue

        net_salary = calculateSalary(salary.base_salary, attendance.hours_worked // 8)
        bonus_value = calculateBonus(salary.base_salary, attendance, bonus) if bonus else 0
        total_salary = round(net_salary + bonus_value, 2)
        brut = salary.base_salary
        cas = brut * 0.25
        cass = brut * 0.10
        impozit = brut * 0.10

        file_path = os.path.join(PDF_FOLDER, f"payslip_{emp.id_employee}.pdf")
        pdf = canvas.Canvas(file_path,encrypt=emp.cnp, pagesize=A4)
        width, height = A4
        y = height - 50

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(width / 2, y, "Pay slip")
        y -= 25
        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(width / 2, y, f"{luna_text} {anul}")
        y -= 10

        pdf.setLineWidth(0.5)
        pdf.line(30, y, width - 30, y)
        y -= 30

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "Full name:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(200, y, f"{emp.first_name} {emp.last_name}")
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "CNP:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(200, y, emp.cnp)
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "Email:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(200, y, emp.email)
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "ID Employee:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(200, y, emp.id_employee)
        y -= 10

        pdf.line(30, y, width - 30, y)
        y -= 30

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "Base salary:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(250, y, f"{brut:.2f} RON")
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "CAS (25%):")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(250, y, f"{cas:.2f} RON")
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "CASS (10%):")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(250, y, f"{cass:.2f} RON")
        y -= 20

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, y, "Impozit (10%):")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(250, y, f"{impozit:.2f} RON")
        y -= 20

        pdf.line(30, y, width - 30, y)
        y -= 25

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Bonuses:")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(250, y, f"{bonus_value:.2f} RON")
        y -= 20

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "NET Salary:")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(250, y, f"{net_salary:.2f} RON")
        y -= 20

        pdf.line(30, y, width - 30, y)
        y -= 25

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Total:")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(250, y, f"{total_salary:.2f} RON")

        pdf.setFont("Helvetica-Oblique", 9)
        pdf.setFillColor(colors.grey)
        pdf.drawRightString(width - 30, 30, "Automatically generated")

        pdf.save()

