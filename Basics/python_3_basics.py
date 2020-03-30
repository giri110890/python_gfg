# python code for "Hello World"

print("Hello World")

# python code to declare variables

myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber = "helloworld"
print(myNumber)

# python program to illustrate the list

# created a empty list
nums = []

#appending the data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)

#Python program to ilustrate 
#getting input from the user
name = input("Enter your name: ")

#see the name user has entered
print("hello", name)

#python3 program to get input from user

#accepting integer from the user
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

#Python program to illustrate if-else
#selection statement
num1 = 34
if (num1 > 12):
    print("Num1 is good")
elif (num1 > 35):
    print("Num2 is not gooo......")
else:
    print("Num2 is great")


#Python program to illustrate 
#functions
def hello():
    print("hello")
    print("hello again")

#calling function
hello()

#Python program to illustrate
#function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result

def Main():
    print("Started")
# calling the getInteger function and
# storing its returned value in the output variable
    output = getInteger()
    print(output)

# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    Main()

# Python program to illustrate
# a simple for loop
for step in range(1, 5, 2):
    print(step)

# Python program to illustrate
# math module
import math

def makeFloatAbs():
    num = float(input("Enter a number: "))
    # fabs is used to get the absolute value of a decimal
    num = math.fabs(num)
    print(num)
if __name__ == "__main__":
    makeFloatAbs()
