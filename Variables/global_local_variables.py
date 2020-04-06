# This function uses global variable s
def f():
    print (s)

# Global scope
s = "I love GeeksForGeeks"
f()

# This function has a variable with
# name same as s
def f1():
    global s
    print(s)
    s = "Me too."
    print(s)

# Global scope
s = "I love Geeksforgeeks"
f1()
print(s)

# A good example
a = 1
# uses global because there is no local 'a'
def f2():
    print("Inside f2() : ", a)

# Variable 'a' is redefined as a local
def g():
    a = 2
    print("Inside g() : ", a)

# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print("Inside h() : ", a)

# Global scope
print("global : ", a)
f2()
print("global : ", a)
g()
print("global : ", a)
h() 
print("global : ", a) 
