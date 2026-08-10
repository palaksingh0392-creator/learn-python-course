# SalaryCalculator
#Take basic salary, bonus and tax percentage. Find gross salary, tax amount and final salary
salary = float(input("enter the amount of salary:"))
bonus = float(input("enter the amount of bonus:"))
tax = float(input("enter the amount of tax in percent:"))

gross = salary + bonus 
final = gross - tax

print(f"the salary is {salary}, bonus {bonus}, tax {tax} ")
print(f"the calculated gross salary {gross}")
print(f"the final salary {final}")
