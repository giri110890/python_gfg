# Conditions in Python

a = 3
b = 9
if (b % a == 0):
    print("{} is divisible by {}".format(a, b))
elif (b + 1 == 10): 
    print("Increment in b produces 10")
else:
    print("You are in else statement")

# Functions in Python

# Function for checking the divisibility
# Notice the identation after function declaration
# and if and else statements
def checkDivisibilty(a, b):
    if (a % b == 0):
        print ("a is divisible by b")
    else:
        print("a is not divisible by b")
    
checkDivisibilty(4, 2)