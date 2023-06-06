"""write a program that prompts the user for a list of numbers and prints out the maximum and
minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes."""""
User_Input = []
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
maximum = max(User_Input)
lowest = min(User_Input)
print(User_Input)
print(f"Muximum is:{maximum}" )
print(f"Mimum is:{lowest} ")
print(f"Muximum is:{maximum}", f"\nMinimum is:{lowest}")
print(f"Muximum is:{maximum}\nMinimum is:{lowest}")
print("Max is" +str(maximum) +"and" "min is"+str(lowest))

