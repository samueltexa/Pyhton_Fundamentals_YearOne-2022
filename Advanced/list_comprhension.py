#creating a list squared numbers by traditional loop
list = []
for i in range (10):
    squared_numbers = (list.append(i**2))
print(list)

# by list comprehenssion

squared_number = [i ** 2 for i in range(10)]
print(squared_number)