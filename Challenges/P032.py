import math

r = float(input("Enter the radius of a cirlce area:").strip())
d = float(input("Enter the depth of a cylinder:").strip())

v = ((math.pi * r) ** 2) * d

print("The total volume is: "+str(v))
