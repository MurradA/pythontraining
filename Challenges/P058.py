import random

score = 0

for x in range(1, 6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    calc = num1 + num2
    question = int(input("{0} + {1} = ".format(num1, num2)).strip())
    if question == calc:
        score += 1

if score == 5:
    print("Congratulations you got 5/5 correct")
else:
    print("Good try, you got {0}/5 correct!".format(score))

