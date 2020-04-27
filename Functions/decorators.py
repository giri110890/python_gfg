'''

In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and
returned from other functions as well.

Functions can be defined inside another function and can also be passed 
as argument to another function.


# Syntax for decorator

@gfg_decorator
def hello_decorator():
    print("GFG")


Above code is equivalent to

def hello_decorator():
    print("GFG")

hello_decorator = gfg_decorator(hello_decorator)'''


# Decorator can modify the behaviour
def hello_decorator(func):
    # inner1 is a Wrapper function in which the argument is called

    # inner function can access the outer local functions like in this
    # case func
    def inner1():
        print("Heelo, this is before function execution")

        # calling the actual function now inside the wrapper function
        func()
        print("This is after function execution")
    
    return inner1

# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")

# passing 'function_to_be_used' inisde the decorator to control its
# behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function 
function_to_be_used()


# program to find out the execution time of a function using a decorator

# importing libraries
import time
import math

# decorator to calculate duration taken by any function
def calculate_time(func):

    # added arguments inside the inner1, if function takes any arguments
    # can be added like this
    def inner2(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        func(*args, **kwargs)
        # storing time after function execution 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
    
    return inner2

# this can be added to any function present, in this case to 
# calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time so that you can
    # see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function
factorial(10)

# What if a function returns something
def hello_decorator_new(func):
    def inner_new(*args, **kwargs):
        print("before Execution")

        # getting the return value
        returned_value = func(*args, **kwargs)
        print("After execution")

        # return the value to the original frame
        return returned_value
    return inner_new

# adding decorator to the function
@hello_decorator_new
def sum_two_number(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2
# getting the value through return of the function 
print("Sum =", sum_two_number(a, b))