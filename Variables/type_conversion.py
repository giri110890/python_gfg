# Python code to demonstrate Type conversion
# using int(), float()

# Initializing string
s = "10010"

# prinitng string converting to int base 2
c = int(s, 2)
print("After converting to integer base 2 : " \
        , end = "")
print(c)

# printing string converting to float
e = float(s)
print("After converting to float : ", end = "")
print(e)

# Python code to demonstrate Type conversion
# using ord(), hex(), oct()

# initializing integer
s = '4'

# printing character converting to integer
# returns the ASCII code
c = ord(s)
print("After converting character to integer : "
        , end = "")
print(c)

# prinitng integer converting to hexadecimal string
c = hex(56)
print("After converting 56 to hexadecimal string : "
    , end = "")
print(c)

# prinitng integer converting to octal string
c = oct(56)
print("After converting 56 to octal string : ", end = "")
print(c)

# Python code to dmonstrate Type conversion
# using tuple(), set(), list()

# initializing the string
s = "geeks"

# printing string converting to tuple
c = tuple(s)
print("After converting to tuple : ", end = "")
print(c)

# printing string converting to set
c = set(s)
print("After converting to set : ", end = "")
print(c)

# printing string conversion to list
c = list(s)
print("After converting to list : ", end = "")
print(c)

# Python code to demonstrate Type conversion 
# using  dict(), complex(), str() 
  
# initializing integers 
a = 1
b = 2
  
# initializing tuple 
tup = (('a', 1) ,('f', 2), ('g', 3)) 
  
# printing integer converting to complex number 
c = complex(1,2) 
print ("After converting integer to complex number : ",end="") 
print (c) 
  
# printing integer converting to string 
c = str(a) 
print ("After converting integer to string : ",end="") 
print (c) 
  
# printing tuple converting to expression dictionary 
c = dict(tup) 
print ("After converting tuple to dictionary : ",end="") 
print (c) 


