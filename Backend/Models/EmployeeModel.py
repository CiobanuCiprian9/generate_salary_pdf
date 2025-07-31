from extensions import db

class Employee(db.Model):
    __tablename__='Employees'

    id_employee=db.Column(db.String(10),primary_key=True,nullable=False,unique=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    cnp=db.Column(db.String(13),nullable=False,unique=True)
    email=db.Column(db.String(120),nullable=False,unique=True)
    id_manager=db.Column(db.String(10),db.ForeignKey('Employees.id_employee'))