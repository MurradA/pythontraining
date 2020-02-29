from array import *
import random

num1 = array('i',[])

num2 = array('i',[])

for i in range(0,3):
    num = int(input("Enter a number: ").strip())
    num1.append(num)

for i in range(0,5):
    i = random.randint(1, 100)
    num2.append(i)

num1.extend(num2)

for i in num1:
    print(i)

