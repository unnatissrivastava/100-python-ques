#map() converts elements from string to int, since .split() only accepts string values
x,y,z = map(int, input("Enter three numbers: ").split())
op = x**2 + y**2 + z**2
print(op)
