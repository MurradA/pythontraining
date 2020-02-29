bill = float(input("Enter the total bill amount:".strip()))
total_diners = int(input("How many diners are there?:".strip()))
sum = bill/total_diners
print("Each diner must pay £{0}.".format("%.2f" % sum))
