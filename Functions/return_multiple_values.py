# A python program to return multiple values from a method using class
class Test:
    def __init__(self):
        self.str = "geeksfor geeks"
        self.x = 20
    
# This function returns an object of Test
def fun():
    return Test()

# Driver code to test above method
t = fun()
print(t.str)
print(t.x)

# A Python program to return multiple  
# values from a method using tuple 

def funTuple():
    str = "geeksforgeeks"
    x = 20
    return (str, x) # Return tuple, we could also # write (str, x)

# Driver code to test above method
str, x = funTuple()
print(str)
print(x)


# A Python program to return multiple  
# values from a method using list 
  
# This function returns a list 
def funList(): 
    str = "geeksforgeeks"
    x = 20   
    return [str, x]
  
# Driver code to test above method 
list = funList()  
print(list)


# A Python program to return multiple  
# values from a method using dictionary 
  
# This function returns a dictionary 
def funDict(): 
    d = dict()
    d['str'] = "GeeksforGeeks"
    d['x']   = 20
    return d 
  
# Driver code to test above method 
d = funDict()  
print(d) 










