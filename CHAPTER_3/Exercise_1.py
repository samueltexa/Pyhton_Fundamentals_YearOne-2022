# Rewrite your pay computation to give the employee 1.5 times the hourly
# rate for hours worked above 40
# hours = 45, rate = 10, pay = 475.0
hours = float(input("Enter hours:"))
hourly_rate = float(input("Enter rate:"))


def Above_40():
    Extra_time = (1.5 * hours) * hourly_rate
    print("Pay for hours worked above 40 is:", Extra_time)


def working():
    if hours > 40:
        Above_40()
    else:
        print("It's below 40.")


working()
