# Logical operators are used to combine conditional statements:

# Example

# 1.and. Returns True if both statements are true
num1 = 3
num2 = 4
num3 = 2
print(num1<num2 and num2>num3)
print(num2<num1 and num2>num3)

# 2.or. Returns True if one of the statements is true
print(num1<num2 or num2>num3)
print(num2<num1 or num2>num3)
print(num2<num1 or num2<num3)

# 3.not. Reverse the result, returns False if the result is true
print(not(num1<num2 and num2>num3))
print(not(num2<num1 or num2<num3))