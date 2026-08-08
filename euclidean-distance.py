import math
x1 = int(input("enter the value of co-ordinate 1 at x axis: "))
x2 = int(input("enter the value of co-ordinate 2 at x axis: "))
y1 = int(input("enter the value of co-ordinate 1 at y axis: "))
y2 = int(input("enter the value of co-ordinate 2 at y axis: "))
euclidean_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("the euclidean distance of two co-ordinates is ",euclidean_dist)
