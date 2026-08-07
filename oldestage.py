age1 = int(input("enter 1st age"))
age2 = int(input("enter 2nd age"))
age3 = int(input("enter 3rd age"))
if age1 > age2 and age1 > age3:
    print("age1 is the oldest age")
elif age2>age3 and age2 > age1:
    print("age2 is the oldest age")
else:
    print("age3 is the oldest age")
