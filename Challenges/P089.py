from array import *
import random

num = array('i',[])

for i in range(0,5):
    randomint = random.randint(1, 100)
    num.append(randomint)

for i in num:
    print(i)
