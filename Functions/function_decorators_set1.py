# A python program to demonstrate that a function can be defined inside
# another function and a function can be passed as parameter

# Adds a welcome message to the string
def messageWithWelcome(o):

    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome() and str
    return addWelcome() + o

# To get site name to which welcome is added
def site(site_name):
    return site_name

print(messageWithWelcome(site("GeeksForGeeks")))

# A decorator is a function that takes a function as its only parameter 
# and returns a function.his is helpful to “wrap” functionality with the
#  same code over and over again.


# We use @func_name to specify a decorator to be applied on another 
# function.

# Adds a welcome message to the string returned by fun(). Takes fun() as
# parameter and returns welcome()
def decorate_message(fun):

    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)
    
    # Decorator returns a fucntion
    return addWelcome

@decorate_message
def sitenew(site_name):
    return site_name

# Driver code 
  
# This call is equivalent to call to 
# decorate_message() with function 
# sitenew("GeeksforGeeks") as parameter 
print (sitenew("VEndiway"))

# Decorators can also be useful to attach data(or add attribute) to
# functions

# A Python example to demonstrate that decorators can be useful attach
# data

# A decorator function to attach data to func
def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x, y):
    return x + y

# Driver Code

# This call is equivalent to attach_data() with add() as parameter
print(add(2, 3))
print(add.data)
