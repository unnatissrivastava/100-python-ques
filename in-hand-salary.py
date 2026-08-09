salary = float(input("Enter your salary (in lakhs): "))

hra = salary * 0.10
da = salary * 0.05
pf = salary * 0.03

after_deductions = salary - hra - da - pf

if 0 <= salary <= 1:
    tax = 0
elif 5 <= salary <= 10:
    tax_rate = 0.10
    tax = after_deductions * tax_rate
elif 11 <= salary <= 20:
    tax_rate = 0.20
    tax = after_deductions * tax_rate
elif salary > 20:
    tax_rate = 0.30
    tax = after_deductions * tax_rate
else:
    tax = 0 

in_hand = after_deductions - tax
print("In-hand salary is:", in_hand)
