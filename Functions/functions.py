# A Simple python function to check whethr x is even or odd

def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("Odd")

# Driver Code
evenOdd(5)
evenOdd(6)

# One important thing to note is, in Python every variable name is a 
# reference.When we pass a variable to a function, a new reference to the 
# object is created. Parameter passing in Python is same as reference 
# passing in Java.

# Her x is a new refernce to same list lst
def myFun(x): 
   x[0] = 20
  
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst)
print(lst)

# when we pass a reference and change the received reference to something
# else, the connection between passed and received parameter is broken.
# For example consider below program

def myFun1(x):

    # After below line link of x with previous object gets broken. A new
    # object is assigned to x
    x = [20, 30, 40]

# Driver Code (Note that lst is not modified)
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun1(lst)
print(lst)

def myFun2(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = 20
  
# Driver Code (Note that lst is not modified 
# after function call. 
x = 10 
myFun2(x)
print(x)


def swap(x, y): 
    temp = x
    x = y
    y = temp 
  
# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y)

# Like C++ default arguments, any number of arguments in a function can 
# have a default value. But once we have a default argument, all the
# arguments to its right must also have default values.

# Python program to demonstrate default arguments
def myFun3(x, y = 50, z = 10):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only 
# argument) 
myFun3(10)

# Te idea is to allow caller to specify argument name with values so that 
# caller does not need to remember order of parameters.

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)

# Keyword arguments
student(firstname = "Geeks", lastname = "Practice")
student(lastname = "Punnamaraju", firstname = "Giridhar")

# Python program to illustrate *args for variable number of arguments
def myFun4(*argv):
    for arg in argv:
        print(arg)
myFun4('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate *kwargs for variable number of keyword
# arguments

def myFun5(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
# Driver code 
myFun5(first ='Geeks', mid ='for', last='Geeks') 

# In Python anonymous function means that a function is without a name
# As we already know that def keyword is used to define the normal
# functions and the lambda keyword is used to create anonymous functions.

# Python code to illustrate cube of a number
# using lambda function

cube = lambda x: x*x*x
print(cube(7))