# created a class named MyClass
class MyClass:
    # assign the values to Myclass attributes
    number = 0
    name = "noname"

def Main():
    # Creating an object of the MyClass
    # Here, 'me' is the object
    me = MyClass()

    # Accessing the attributes of MyClass
    # using the dot(.) operator
    me.number = 1337
    me.name = "Harssh"

    #str is an in built function that creates an string
    print(me.name + " " + str(me.number))

# telling python that there is main in the program
if __name__ == "__main__":
    Main()

'''
2. Methods

Method is a bunch of code that is intended to perform a particular task 
in your Python’s code.

Function that belongs to a class is called an Method.

All methods require ‘self’ parameter. If you have coded in other OOP 
language you can think of ‘self’ as the ‘this’ keyword which is used for 
the current object. It unhides the current instance variable.’self’ 
mostly work like ‘this’.

‘def’ keyword is used to create a new method.
'''

# A Python program to demonstrate working of class methods
class vector2D:
    x = 0.0
    y = 0.0

    # Creating a method named Set
    def Set(slef, x, y):
        self.x = x
        self.y = y

def Main1():
    # vec is an object of class Vector2D
    vec = vector2D()
    # PAssing values to the function set by using dot(.) operator
    vec.Set(5, 6)
    print("X: " + str(vec.x) + ", Y: " + str(vec.y))

if __name__ == "__main__":
    Main1()

'''
3. Inheritance

Inheritance is defined as a way in which a particular class inherits 
features from its base class.Base class is also knows as ‘Superclass’ 
and the class which inherits from the Superclass is knows as ‘Subclass’

# Syntax for inheritance 
  
class derived-classname(superclass-name)

'''
# A Python Program to demonstrate working of inheritance
class Pet:
    # __init__ is an constructor in Python
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class Cat inheriting from the class Prt
class Cat(Pet):
    def __init__(self, name, age):
        # Calling the super-class function __init__ using the super()
        # function
        super().__init__(name, age)


def Main2():
    thePet = Pet("Pet", 1)
    jess = Cat("Jess", 3)

    # isinstance() function to check whether a class is inherited from 
    # another class
    print("Is Jess a cat? " + str(isinstance(jess, Cat)))
    print("Is jess a pet? " +str(isinstance(jess, Pet))) 
    print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
    print("Is thePet a Pet? " +str(isinstance(thePet, Pet)))
    print(jess.name)

if __name__=="__main__":
    Main2()

