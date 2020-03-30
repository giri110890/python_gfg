# in C++/C user can take multiple inputs in one line
# using scanf but in Python user can take multiple
# values or inputs in one line by two methods.

# using split() method
# syntax input().split(separator, maxsplit)

# Python program showing how to take
# multiple input using split

# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Total number of boys: ", y)
print("Total number of girls: ", z)
print()


# taking two inputs at a time
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}"
    .format(a, b))
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)

# python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is: ", x)
print("Second nuber is: ", y)
print()

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print("Third number is: ", z)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)