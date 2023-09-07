"""The tuple is another data type which is a sequence of data similar to a list. But it is immutable.
That means data in a tuple is write-protected. Data in a tuple is written using parenthesis and commas."""
# Example
#tuple having only integer type of data.
a=(1,2,3,4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"

mytuple = [1,2,3],[3,5,6,7],[9,0]
print(mytuple)
print(mytuple[0])
print(len(mytuple))