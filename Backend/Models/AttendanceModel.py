from extensions import db

class Attendance(db.Model):
    __tablename__="Attendance"

    id = db.Column(db.Integer, primary_key=True)
    id_employee = db.Column(db.String(10), db.ForeignKey('Employees.id_employee'), nullable=False)
    hours_worked=db.Column(db.Integer,nullable=False)
    hours_overtime=db.Column(db.Integer,nullable=False)
    hours_weekend=db.Column(db.Integer,nullable=False)
    hours_holiday=db.Column(db.Integer,nullable=False)
    day_vacation=db.Column(db.Integer,nullable=False)
    month=db.Column(db.Date,nullable=False)