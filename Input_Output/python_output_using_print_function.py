# Python 3.X program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x) # output x = 5

# output can only concatenate string not int
# notice the space difference before and after
print("x =" + str(x)) # output x =5 

# code for disabling the softspace feature
print('G', 'F', 'G', sep = '')

# code without softspace feature
print('G', 'F', 'G')

# using end argument
print("Python", end= '@')
print("GeeksforGeeks")                