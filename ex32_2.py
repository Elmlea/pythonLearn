the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first lind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} as we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i) # I presume it appends an item to a list..!

# now we can print them out too
for i in elements:
    print(f"Element was {i}")

# trying Study Drill 2
elements = range(0,6)

for i in elements:
    print(f"Adding {i} to the list, I hope...!")

# This section sets elements as an implicit list by assigning it to range(0,6)
# It then generates a variable i, and compares that to the first part of the list
# We then iterate through
