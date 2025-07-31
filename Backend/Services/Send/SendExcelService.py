import smtplib
from email.message import EmailMessage
from Services.zip.arhiveService import add_to_arhive

from Models.EmployeeModel import Employee
import os

from dotenv import load_dotenv
load_dotenv()

def sendExcel():
    managers = Employee.query.filter(Employee.id_employee.like("M%")).all()

    EXCEL_FOLDER = "reports/excel_reports"

    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 25
    smtp_user = os.environ.get("MAILTRAP_USER")
    smtp_pass = os.environ.get("MAILTRAP_PASSWORD")

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.login(smtp_user, smtp_pass)

        for mgr in managers:
            try:
                file=f"manager_{mgr.id_employee}.xlsx"
                file_path = os.path.join(EXCEL_FOLDER, file)
            except Exception as e:
                print("File not found")

            email = EmailMessage()
            email['Subject'] = "Raport lunar angajati"
            email['From'] = os.environ.get('MAILTRAP_USER')
            email['To'] = mgr.email

            with open(file_path, "rb") as content_file:
                content = content_file.read()

            email.add_attachment(content,maintype="application",subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",filename=file)

            try:
                smtp.send_message(email)
                print("Trimite Excel")
            except Exception as e:
                print(f"Eroare la: {e}")

def excelReady():
    os.makedirs("flags", exist_ok=True)
    open("flags/excel_ready.flag", "w").close()

    if os.path.exists("flags/pdf_ready.flag"):
        add_to_arhive()