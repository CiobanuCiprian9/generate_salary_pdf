\# Employee Payroll System



A Python Flask application that generates salary slips (PDF) and monthly reports (Excel) for employees, sends them via email and archives the files into a single ZIP.



---



\##  Features



* Generates a PDF salary slip for each employee
* Generates an Excel report for each manager (with their direct employees)
* Sends emails with personalized attachments (PDF to employees, Excel to managers)
* Automatically triggers ZIP archive creation after both processes complete, regardless of order



---



\##  Endpoints



GET /createAggregatedEmployeeData - creates the Excel

GET /createPdfForEmployees - creates the PDF

GET /sendAggregatedEmployeeData - sends the Excel to manager via email

GET /sendPdfToEmployees - send the PDF to employee via email



---



\## Technologies Used



* Python 3.10+
* Flask
* SQLAlchemy
* Pandas
* reportlab
* smtplib (email)
* Mailtrap (for safe testing)
