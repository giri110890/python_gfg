# Syntax [on_true] if [expression] else [on_false] 

# Simple Method to use ternary operator:
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)

# 2. Direct Method by using tuples, Dictionary and lambda

# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
print((b, a) [a < b])

# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b])

# lamda is more efficient than above two methods 
# because in lambda  we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]())

# 3. Ternary operator can be written as nested if-else

# Python program to demonstrate nested ternary operator 
a, b = 10, 20
  
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")


# Python program to demonstrate nested ternary operator 
a, b = 10, 20
  
if a != b: 
    if a > b: 
        print("a is greater than b") 
    else: 
        print("b is greater than a") 
else: 
    print("Both a and b are equal")
