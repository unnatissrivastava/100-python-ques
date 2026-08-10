total_heads = int(input("Enter total heads: "))
total_legs = int(input("Enter total legs: "))

dogs = (total_legs - 2 * total_heads) / 2
chickens = total_heads - dogs

print("Dogs:", dogs)
print("Chickens:", chickens)
