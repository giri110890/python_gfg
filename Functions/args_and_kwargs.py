# Python program to illustrate   
# *args for variable number of arguments

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate **kwargs for variable number of keyword
# arguments

def myFun1(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# Driver code
myFun1(first = 'Geeks', mid = 'for', last = 'Geeks')

# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument. 
  
def myFun3(arg1, **kwargs): 
    print(arg1)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun3("Hi", first ='Geeks', mid ='for', last='Geeks')

# Using *args and **kwargs to call a function

def myFun4(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now we can use *args or **kwargs to pass arguments to this function:
args = ("P", "v", "r")
myFun4(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun4(**kwargs) 

# Using *args and **kwargs in same line to call a function
def myFun5(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun5('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")