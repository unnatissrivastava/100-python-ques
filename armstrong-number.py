number = int(input("Enter a number: "))
original = number         
num_digits = len(str(number))  

total_sum = 0

while number > 0:
    digit = number % 10
    total_sum = total_sum + digit ** num_digits  
    number = number // 10

if total_sum == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
