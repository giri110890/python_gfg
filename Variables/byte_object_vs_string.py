# Python code to demonstrate String encoding

# initializing a String
a = 'GeeksforGeeks'

# Initializing a byte object
c = b'GeeksforGeeks'
print(c)

# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mappping
d = a.encode('ASCII')
print(d)

# checking if a is converted to bytes or not
if (d == c):
    print("Encoding successful")
else:
    print("Encoding Unsuccessful")

# Python code to demonstrate Byte Decoding

# initializing a String
a = "GeeksforGeeks"

# initializing a byte object
c = b'GeeksforGeeks'

# using decode() to decode the Byte object
# decoded version of c is stored in d
# using ASCII mapping
d = c.decode("ASCII")

# checking if c is converted to String or not
if (d == a):
    print("Decoding Successful")
else :
    print("Decoding Unsuccessful")
