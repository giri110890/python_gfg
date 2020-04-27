# Strings are arrays of bytes representing Unicode 
# characters.
# python does not have a character data type, a single
# character is simply a string with a length of 1

# Strings can be created using single quotes or double
# quotes or even triple quotes

# Python program for Creation of String

# Creating a String with single quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Create a String with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with a triple Quotes
String1 = '''I'm a Geek and I live in the world of "geeks" \
            '''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)

# Python Program to Access
# characters of string

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

#Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

# Python Program to
# demonstrate tring slicing

# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + 
        "3rd and 2nd last character: ")
print(String1[3:-2])

# Python Program to Update
# character of a String
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character
# of the String
'''String1[2] = 'p'
print("\nUpdating character at 2nd Index: ")
print(String1)'''

# Updating Entire String:
# Python Program to Update
# entire String
String1 = "Hello, I'm a Geek"
print("Initial String")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)


# Deletion of a character

# Python Program to Delete
# characters from a String
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
# del String1[2]
# print("\Deleting character at 2nd Index: ")
# print(String1)

# Python Program to Delete
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
#del String1
print("\nDeleting entire String: ")
print(String1)

# Python program for
# escape sequencing
# of string

# initial string
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quptes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscapingi Backlashes: ")
print(String1)

# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinintg in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw string to
# ignore Escape Sequences
String1 = R"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Fromat: ")
print(String1)

# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format("Geeks", "For", "Life")
print("Print String in default order: ")
print(String1)

# Postiotional formatting
String1 = "{1} {0} {2}".format("Geeks", "For", "Life")
print("\nPrint String in Positional order: ") 
print(String1)

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For',
         l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1)

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for',
            'Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)

# To demonstrate aligning of spaces  
String1 = "\n{} was founded in {}!".format("GeeksforGeeks",
         2009) 
print(String1)

# To demonstrate aligning of spaces  
String1 = "\n{0:<16} was founded in {1:<9}!" \
        .format("GeeksforGeeks", 2009) 
print(String1)

