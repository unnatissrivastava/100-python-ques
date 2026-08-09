t = float(input("What is the temperature?: "))
h = float(input("Enter the amount of humidity present: "))

if t >= 30 and h >= 90:
    print("Weather is HOT AND HUMID")
elif t >= 30 and h < 90:
    print("Weather is HOT")
elif t<30 and h >= 90:
    print("Weather is COOL AND HUMID")
elif t<30 and h <90:
    print("Weather is COOL")
else:
    print("INVALID INFORMATION")
