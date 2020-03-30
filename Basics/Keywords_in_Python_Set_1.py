print(False == 0)  #output True
print(True == 0)   #output False
print(True + True + True) #output 3

# and operator --- return the first false value.if not found return last
print(3 and 0) #output 0
print(3 and 10) #output 10

# or operator --- return the first True value. if not found return last
print(3 or 0) #output 3
print(3 or 10) #output 3

#evaluation happening from right
print(50 or 20 or 30 or 10 or 10) #output 50
print(0 or 3 and 1 or 10 and 1) # output 1

print(1 and 20 and 30 and 10 and 70) #output 70

#Python code to demonstrate True, False, None
#and, or and not

#Showing that None is not equal to 0
#prints False as its false
print(None == 0)

#showing objective of None
#two None value equated to None
#here x and y both are null
#hence true
x = None
y = None
print(x == y)

#showing logical operation
#or (returns True)
print(True or False)

#and (returns False)
print(False and True)

#showing logical operation
#not (returns False)
print(not False)

#Python code to demonstrate
#del and assert keywords

#initializing the list
a = [1, 2, 3]

#printing list before deleting any value
print("The list before deleting any value")
print(a)

# using del to delete the 2nd element of list
del a[1]

#printing list after deleting 2nd element
print("The list after deleting the second element")
print(a)

#demonstrating use of assert
#prints AssertionError
assert 5 < 3, "5 is not smaller than 3"
