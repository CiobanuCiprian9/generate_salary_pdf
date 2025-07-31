from extensions import db

class Bonus(db.Model):
    __tablename__='Bonus'

    id = db.Column(db.Integer, primary_key=True)
    id_employee=db.Column(db.String(10),db.ForeignKey('Employees.id_employee'),nullable=False)
    apply_bonus_overtime=db.Column(db.Boolean,nullable=False)
    apply_bonus_weekend=db.Column(db.Boolean,nullable=False)
    apply_bonus_holiday = db.Column(db.Boolean, nullable=False)