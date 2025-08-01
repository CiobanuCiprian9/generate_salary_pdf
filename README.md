\# Employee Payroll System


This application automates the generation and distribution of payroll documents for employees and managers. It generates individual *PDF payslips* for employees, manager-specific Excel reports summarizing team salary data, and archives both formats into a single downloadable ZIP file. The system also emails the appropriate files to recipients using *Mailtrap* for safe testing.



---



\##  Features



* Generates a PDF salary slip for each employee
* Generates an Excel report for each manager (with their direct employees)
* Sends emails with personalized attachments (PDF to employees, Excel to managers)
* Automatically triggers ZIP archive creation after both processes complete, regardless of order



---



\##  Endpoints



POST /createAggregatedEmployeeData - creates the Excel

POST /createPdfForEmployees - creates the PDF

POST /sendAggregatedEmployeeData - sends the Excel to manager via email

POST /sendPdfToEmployees - send the PDF to employee via email



---



\## Technologies Used



* Python 3.10+
* Flask
* SQLAlchemy
* Pandas
* reportlab
* smtplib (email)
* Mailtrap (for safe testing)
