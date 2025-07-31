
def calculateSalary(base_salary,days_worked):
    brut_per_hour=base_salary/160
    brut_worked=brut_per_hour*days_worked*8

    pensie=brut_worked*25/100
    cass=brut_worked*10/100
    impozit=brut_worked*10/100


    salary_paid=brut_worked-pensie-cass-impozit

    return round(salary_paid,2)