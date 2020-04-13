# Assigning is not performed in case of immutable containers, 
# such as strings, numbers and tuples.

# Python code to demonstrate the working of  
# iadd() and iconcat() 
  
# importing operator to handle operator operations 
import operator 

a = 2
b = 3  
# using iadd() to add and assign value 
a = operator.iadd(a, b)

# printing the modified value 
print ("The value after adding and assigning : ", end="") 
print (a)

# initializing values 
y = "geeks"
  
z = "forgeeks"
  
# using iconcat() to concat the sequences 
y = operator.iconcat(y, z) 
  
# using iconcat() to concat sequences  
print ("The string after concatenation is : ", end="") 
print (y)

# Python code to demonstrate the working of  
# isub() and imul() 
  
# importing operator to handle operator operations

# using isub() to subtract and assign value 
x = operator.isub(2, 3)
  
# printing the modified value 
print ("The value after subtracting and assigning : ", end="") 
print (x) 
  
# using imul() to multiply and assign value 
x = operator.imul(2, 3)
  
# printing the modified value 
print ("The value after multiplying and assigning : ", end="") 
print (x)

# Python code to demonstrate the working of  
# itruediv() and imod()

# using itruediv() to divide and assign value 
x = operator.itruediv(10, 5); 
  
# printing the modified value 
print ("The value after dividing and assigning : ", end="") 
print (x) 
  
# using imod() to modulus and assign value 
x = operator.imod(10.0, 6)
  
# printing the modified value 
print ("The value after modulus and assigning : ", end="") 
print (x)




