# Example of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
# Division(float) of number
div1 = a / b
# Division(floor) of umber
div2 = a // b
# Modulo of both number
mod = a % b

# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

# Examples of Relational Operators
a = 13
b = 33

#  a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# Examples of Logical Operator 
a = True
b = False
  
# Print a and b is False 
print(a and b) 
  
# Print a or b is True 
print(a or b) 
  
# Print not a is False 
print(not a)

# Note bitwise operators work only on integers 
# Example of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
# Python Ones’ complement of a number ‘A’ is equal to -(A+1).
print(~a)

# print bitwise XOR operation
# Python bitwise XOR operator returns 1 if one of the bits is 0 and 
# the other bit is 1. If both the bits are 0 or 1, then it returns 0.
print(a ^ b)

# print bitwise right shift operation
# Python right shift operator is exactly the opposite of the 
# left shift operator. Then left side operand bits are moved 
# towards the right side for the given number of times. In simple terms, 
# the right side bits are removed.
print(a >> 1)

# print bitwise left shift operation
# Python bitwise left shift operator shifts the left operand 
# bits towards the left side for the given number of times 
# in the right operand. In simple terms, the binary number is 
# appended with 0s at the end.
print(a << 2)

# is and is not are the identity operators both are used to check if
# two values are located on the same part of the memory. Two variables 
# that are equal does not imply that they are identical.
# Examples of Identity operators 
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3]  
print(a1 is not b1)   
print(a2 is b2)   
# Output is False, since lists are mutable. 
print(a3 is b3) 

# Membership operators
# in and not in are the memeber operators, used to test whether a 
# value or variable is in a sequence
# Examples of Membership operator 
x = 'Geeks for Geeks'
y = {3:'a',4:'b'} 
print('G' in x) 
print('geeks' not in x)  
print('Geeks' not in x)   
print(3 in y)
#in is the intended way to test for the existence of a key in a dict.
print('b' in y) 

