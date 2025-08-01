import smtplib
import time
from email.message import EmailMessage
from Models.EmployeeModel import Employee
import os
from Services.zip.arhiveService import add_to_arhive
from dotenv import load_dotenv
load_dotenv()

def sendPdf():
    employees = Employee.query.filter(Employee.id_employee.like("A%")).all()

    PDF_FOLDER = "reports/pdf_payslip"

    smtp_server = "smtp.mail.yahoo.com"
    smtp_port = 587
    smtp_user = os.environ.get("MAILTRAP_USER")
    smtp_pass = os.environ.get("MAILTRAP_PASSWORD")

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login( smtp_user, smtp_pass)

        for i,emp in enumerate(employees):
            try:
                file=f"payslip_{emp.id_employee}.pdf"
                file_path = os.path.join(PDF_FOLDER, file)
            except Exception as e:
                "File not found"

            email=EmailMessage()
            email['Subject']='Salary slip'
            email['From']=os.environ.get('MAILTRAP_USER')
            email['To']=emp.email

            with open(file_path,'rb') as content_file:
                content=content_file.read()

            email.add_attachment(content,maintype='application',subtype='pdf',filename=file)

            try:
                smtp.send_message(email)
                if i%5==0:
                    time.sleep(20)
                print("Trimite PDF")
            except Exception as e:
                print(f"Eroare la: {e}")

def pdfReady():
    os.makedirs("flags", exist_ok=True)
    open("flags/pdf_ready.flag", "w").close()

    if os.path.exists("flags/excel_ready.flag"):
        add_to_arhive()