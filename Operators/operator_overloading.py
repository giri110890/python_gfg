# same built-in operator function shows different behaviour for objects
# of different classes , this is called operator overloading

# Pyhton program to show use of 
# + operator for different purposes.
5 + 3
print (1 + 2)

# concatenate two strings
print("Geeks" + "For")

# PRoduct two numbers
print(3 * 4)
# Repeat the String
print("Geeks" * 4)

# Code 1
# Python Program to illustrate how to overload an 
# binary + operator

class A :
    def __init__(self, a):
        self.a = a
    
    # adding two objects
    def __add__(self, o):

        return self.a + o.a
    
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

# Python program to perform addition of two complex numbers using binary
# + operator overloading

class complexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # adding two objects
    def __add__(self, other):
        return(self.a + other.a, self.b + other.b)
    
    def __str__(self):
        return(self.a, self.b)

Ob1 = complexNum(1, 2) 
Ob2 = complexNum(2, 3) 
Ob3 = Ob1 + Ob2 
print(Ob3)

# Python program to overload a comparison operators
class compareOp:
    def __init__(self, a):
        self.a = a
    
    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False
ob1 = compareOp(2)
ob2 = compareOp(3)
if(ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")



