for i in range(5):  # i will be 0, 1, 2, 3, 4
    if i == 2:
        continue  # Skip the rest of the loop for i == 2
    if i == 4:
        break     # Stop the loop completely when i == 4
    print(i)


"""
Iteration breakdown:
i = 0 → not 2, not 4 → print 0

i = 1 → not 2, not 4 → print 1

i = 2 → continue → skip printing → go to next iteration

i = 3 → not 2, not 4 → print 3

i = 4 → break → stop loop immediately (nothing printed)


"""


for i in range(5):
    if i == 2:
        pass   # does nothing
    print(i)

# Pass:  it’s just a placeholder so Python doesn’t throw an error for having an empty block.