"""write a program that prompts the user for a list of numbers and prints out the maximum and
minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes."""""
User_Input = []
results = []
while True:
    number = input("Enter number:")
    try:
        Value_input = int(number)
        User_Input.append(Value_input)
    except ValueError:
        if number == "done":
            break
        else:
            print("Invalid data input.")
maximum = results.append(max(User_Input))
lowest = results.append(min(User_Input))
print(results)
print(User_Input)