# var1 is in the global namespace
var1 = 5
def some_func():

    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():

        # var3 is in the nested local
        # namespace
        var3 = 7
    
# Python program processing
# global variable

count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

# python program showing
# a scope of object
def some__newfunc():
    var = 55555
    print("You aore welcome to some_func")
    print(var)
some__newfunc

# Pytho program showing 
# a scope of object

def some_newfunc():
    print("Inside some function")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
    some_inner_func()
    var = 777
    print("Try printing var from outer function: ",var)
some_newfunc()

