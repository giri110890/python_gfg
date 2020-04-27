''' 
Syntax for decorators with parameters –
@decorator(params)
def func_name():
    Function implementation
The above code is equivalent to

def func_name():
    Function implementation

func_name = (decorator(params))(func_name)
"""
As the execution starts from left to right decorator(params) is called 
which returns a function object fun_obj. Using the fun_obj the call 
fun_obj(fun_name) is made. Inside the inner function, required operations 
are performed and the actual function reference is returned which will be 
assigned to func_name. Now, func_name() can be used to call the function 
with decorator applied on it.
'''
'''
def decorators(*args, **kwargs):
    def inner(func):

        #do operations with func

        return func
    return inner # this is the fun_obj mentioned in the above content

@decorators(params)
def func():
    #function implementation
'''
# Observe these first
# Pythn code to illustrate Decorators basic in Python
def decorator_fun(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        # do operations with func
        func()
    
    return inner
@decorator_fun
def func_to():
    print("Inised actual function")

func_to()

# Another Way

# Python code to illustrate Decorators with parameters in Python
def decorator_fun1(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inisde Inner function new")
        print("DEcorated the new function")
        func()
    
    return inner

def func_to_new():
    print("Inside actual function")

# another way of using decorators
decorator_fun1(func_to_new)()

# Example 1
# Python code to illustrate Decorators with parameters in Python
def decorator(*args, **kwargs):
    print("Inisde decorator")

    def inner(func):
        # code functionality here
        print("Inisde inner function")
        print("I like", kwargs["like"])
        func()

    # returning inner function
    return inner

@decorator(like = "gfg")
def myfunc():
    print("Inside actual function")

# Python code to illustrate Decorators with parameters in Python

def decorator_func(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs):
            print("I like GeeksforGeeks")
            print("summation of values - {}".format(x+y))
            func(*args, **kwargs)
        return wrapper
    return Inner

# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)("Geeks", "for", "Geeks")


