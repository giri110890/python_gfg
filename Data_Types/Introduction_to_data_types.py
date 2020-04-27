# String in python
# sequence of characters
# Strings are immutable ie they cannot be changed

# Assigning string to a variable
a = "This is a string" 
print(a)
print(a[2]) # output i

# Lists in python
# just like arrays
# need not be always homogenous.
# single list can contain strings, integers as well
# as objects
# lists can alos be used to implement stacks & queues
# Lists are mutable ie they can be altered once declared

# Declaring a list
L = [1, "a", "string", 1 + 2]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])

# Tuples in Python
# tuple is a sequence of immutable Python objects
# just like Lists with the exception that tuples
# cannot be changed once declared.
# Tuples are usually faster than lists

tup = (1, "a", "giri", 1 + 2)
print(tup)
print(tup[1])

# Iterations in Python
# example 1 
i = 1
while (i < 10):
    i += 1
    print(i)

# Iteration by for loop on string
s = "Hello World"
for i in s:
    print(i)

# Iteration by for loop on list
L = [1, 4, 5, 7, 8, 9]
for i in L:
    print(i)

# Iteration by for loop for range
for i in range(0, 10):
    print(i)