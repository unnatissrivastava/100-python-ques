P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

A = P*(1 + R/100)**T  
CI = A - P

print("Compound Interest is:", CI)
