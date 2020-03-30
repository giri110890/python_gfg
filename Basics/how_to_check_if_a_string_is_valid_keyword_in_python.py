# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword

# initializing strings for testing
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"
s6 = "shambhavi"
s7 = "True"
s8 = "False"

# checking which are keywords
if keyword.iskeyword(s):
    print( s + " is a python keyword")
else:
    print(s + " is not a python keyword")

if keyword.iskeyword(s1):
    print( s1 + " is a python keyword")
else:
    print(s1 + " is not a python keyword")

# Python code to demonstrate working of kwlist()
print ("The list of keywords is : ")
print (keyword.kwlist) # new extra keywords await and async
