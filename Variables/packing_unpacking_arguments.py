# A python program to demonstrate need
# of packing and unpacking

# A sample function that takes 4 arguments
# and prints them
def fun(a, b, c, d):
    print(a, b, c, d)

# Drive Code
my_list = [1, 2, 3, 4]

# This doesn't work
# fun(my_list)

# Unpacking list into four arguments
fun(*my_list)

# A python program to demonstrate use 
# of packing

# This function uses packing to sum 
# unkown number of arguments
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print(mySum(1, 2, 3, 4))
print(mySum(10, 20))

# A python program to demonstrate bith packing
# and unpacking

# A sample python funtion that takes three arguments
# and prints them
def fun4(a, b, c):
    print(a, b, c)

# Another sample function.
# Tjis is an example of PACKIGN. All arguments passed
# to fun2 are packed into tuple *args
def fun3(*args):
    # Convert args tuple to a list so we cna modify it
    args  = list(args)

    # Modifying args
    args[0] = "GeeksforGeeks"
    args[1] = "awesome"

    # UNPACKING args and calling fun1
    fun4(*args)

# Driver code
fun3("Hello", "giri", "giri!")


# A sample program to demonstrate unpacking of
# dictionary items using **
def funz(a, b, c):
    print(a, b, c)

# A call with unpacking of dictionary
d = {'a' : 2, 'b' : 3, 'c' : 10}
funz(**d)

# A python progem to demonstrate packing f 
# dictionary items using **
def funx(**args):
    # args is a dict
    print(type(args))

    # Prinint dictionary items
    for key in args:
        print("%s = %s" % (key, args[key]))
    
# Drive code
funx(name = "geeks", ID = "101", languages = "Python")
