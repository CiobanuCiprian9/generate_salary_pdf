from Services.Calculate.CalculateSalaryService import calculateSalary

def calculateBonus(base_salary,attendance,bonus):
    salary_per_hour=calculateSalary(base_salary,attendance.hours_worked//8)/160

    bonus_total = 0

    if bonus.apply_bonus_overtime:
        bonus_total += attendance.hours_overtime * salary_per_hour * 1.5

    if bonus.apply_bonus_weekend:
        bonus_total += attendance.hours_weekend * salary_per_hour * 2.0

    if bonus.apply_bonus_holiday:
        bonus_total += attendance.hours_holiday * salary_per_hour * 2.5

    return round(bonus_total,2)