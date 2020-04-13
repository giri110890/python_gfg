# Python code to demonstrate the working of  
# ixor() and ipow() 
  
# importing operator to handle operator operations 
import operator

# using ixor() to exclusive or and assign value 
x = operator.ixor(10,5)

# printing the modified value 
print ("The value after xoring and assigning : ",end="") 
print (x)
# using ipow() to exponentiate and assign value 
x = operator.ipow(5,4);

# printing the modified value 
print ("The value after exponentiating and assigning : ",end="") 
print (x)

# Python code to demonstrate the working of  
# ior() and iand()

# using ior() to or, and assign value 
x = operator.ior(10,5); 
  
# printing the modified value 
print ("The value after bitwise or, and assigning : ",end="") 
print (x) 
  
# using iand() to and, and assign value 
x = operator.iand(5,4); 
  
# printing the modified value 
print ("The value after bitwise and, and assigning : ",end="") 
print (x)

# Python code to demonstrate the working of  
# ilshift() and irshift()

# using ilshift() to bitwise left shift and assign value 
x = operator.ilshift(8,2)

# printing the modified value 
print ("The value after bitwise left shift and assigning : ",end="") 
print (x) 
  
# using irshift() to bitwise right shift and assign value 
x = operator.irshift(8,2); 
  
# printing the modified value 
print ("The value after bitwise right shift and assigning : ",end="") 
print (x)