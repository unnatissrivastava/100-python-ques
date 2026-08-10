while True:
    print("1. cm to ft")
    print("2. km to miles")
    print("3. usd to inr")
    print("4. exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cm = float(input("Enter value in cm: "))
        ft = cm * 0.0328
        print(cm, "cm is", ft, "feet")
    
    elif choice == 2:
        km = float(input("Enter value in km: "))
        miles = km * 0.621
        print(km, "km is", miles, "miles")
    
    elif choice == 3:
        usd = float(input("Enter value in USD: "))
        inr = usd * 83
        print(usd, "USD is", inr, "INR")
    
    elif choice == 4:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice, try again")
