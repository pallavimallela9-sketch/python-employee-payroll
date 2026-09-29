print("==========================================")
print("       EMPLOYEE PAYROLL MANAGEMENT")
print("==========================================")

employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
department = input("Enter department: ")

basic_salary = float(input("Enter basic salary: "))
hra_percentage = float(input("Enter HRA percentage: "))
da_percentage = float(input("Enter DA percentage: "))
deduction = float(input("Enter other deductions: "))

hra = (basic_salary * hra_percentage) / 100
da = (basic_salary * da_percentage) / 100

gross_salary = basic_salary + hra + da
net_salary = gross_salary - deduction

if net_salary < 0:
    net_salary = 0

print("\n==========================================")
print("             PAYROLL DETAILS")
print("==========================================")

print("Employee Name :", employee_name)
print("Employee ID   :", employee_id)
print("Department    :", department)
print("------------------------------------------")
print("Basic Salary  :", basic_salary)
print("HRA           :", hra)
print("DA            :", da)
print("Gross Salary  :", gross_salary)
print("Deductions    :", deduction)
print("Net Salary    :", net_salary)
print("==========================================")

if net_salary >= 50000:
    print("Salary Category: High")
elif net_salary >= 25000:
    print("Salary Category: Medium")
else:
    print("Salary Category: Basic")

print("==========================================")
