# Identity operators are used to compare the objects, not if they are equal, but if they are actually the
# same object, with the same memory location:

# Example

# 1.is. Returns True if both variables are the same object
num1 = 3
num2 = 3
num3 = 4
print(num1 is num2)
print(num1 is num3)

# 2.is not. Returns True if both variables are not the same object
print(num1 is not num2)
print(num1 is not num3)