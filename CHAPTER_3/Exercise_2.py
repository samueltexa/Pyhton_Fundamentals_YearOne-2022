try:
    hours = float(input("Enter hours:"))
    rate = float(input("Enter hours:"))
    if hours > 40:
        Extra_time = (1.5 * hours) * rate
        print(Extra_time)
    else:
        pay = hours * rate
        print(pay)
except ValueError:
    print("Error, please enter numeric input")
