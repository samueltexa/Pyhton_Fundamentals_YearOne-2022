numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i, end=" ")
    
#The range function
for x in range(10):
    print(x)

for y in range(200, 205):
    print(y)
    
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
        print(words)
        
for p in range(0, 10, 3):
    print(p)
    
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
 #break and continue Statements, and else Clauses on Loops   
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
    # loop fell through without finding a factor
        print(n, 'is a prime number')
             
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
    
    
    
    
# While loop
count = 0
while count < 3:
    print(count)
    count += 1