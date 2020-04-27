# A programming language is said to support first-class functions if it treats 
# functions as first-class objects. Python supports the concept of First Class
#  functions.

'''
Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
'''

# Functions are objects
# Python program to illustrate functions can be treated as objects
def shout(text):
    return text.upper()

print(shout("Hello"))
yell = shout
print(yell("Hello"))



# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout1(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print (greeting)  
  
greet(shout1) 
greet(whisper)

# Python program to illustrate functions 
# Functions can return another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10))