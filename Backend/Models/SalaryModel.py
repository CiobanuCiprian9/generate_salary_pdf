from extensions import db

class Salary(db.Model):
    __tablename__='Salaries'

    id = db.Column(db.Integer, primary_key=True)
    id_employee=db.Column(db.String(10),db.ForeignKey('Employees.id_employee'),nullable=False)
    base_salary=db.Column(db.Integer,nullable=False)
    month=db.Column(db.String,nullable=False)