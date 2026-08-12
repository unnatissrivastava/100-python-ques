for num in range(100, 1001):
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num)
