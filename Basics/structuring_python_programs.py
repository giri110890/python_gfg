# Example 1
print('Welcome to Geeks for Geeks')

# Example 2
x = [1, 2, 3, 4]
# x[1:3] means that start from the index 
# 1 and go upto the index 2
print(x[1:3])

""" In the above mentioned format, the first
index is included, but the last index is not
included."""

# Example of multiple statements per line
a = 10; b = 20; c = b + a
print(a); print(b); print(c)

# Bad Practice as width of this code is too much

#code
x = 10
y = 20
z = 30
no_of_teachers = x
no_of_male_students = y
no_of_female_students = z

if (no_of_teachers == 10 and  no_of_female_students == 30 and no_of_male_students == 20):
    print('The course is valid')

# This could be done instead:

if (no_of_teachers == 10 and no_of_female_students ==30
    and no_of_male_students == 20 and x+y == 30):
    print('The course is valid')

# Example 1

# The following code is valid
a = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
    ]
print(a)

# Example 2
# The following code is also valid
person1 = 18
person2 = 20
person3 = 12

if (
    person1 >= 18 and
    person2 >= 18 and
    person3 < 18
    ):
    print("2 persons should have ID cards")

# Explicit Line Continuation
# Example
x = \
    1 + 2 \
    + 5 + 6 \
    + 10

print(x)

""" Readable form could be as follows"""

x = 10
flag = (x == 10) and (x < 12)
print(flag) # output True

# Example

x = [1, 2, 3]
y = 2
a = y in x
print(a) # output True

# Example
print("foo") # Correct
print("foo") # This will generate an error
# The error will be somewhat 'unexpected indent'

# Example
x = 10
while (x != 0):
    if (x > 5): # Line 1
        print("x > 5") # Line 2
    else:   # Line 3
        print("x < 5") # Line 4
    x -= 2 # Line 5
"""
Lines 1, 3, 5 are on the same level
Line 2 will only be executed if if condition becomes true.
Line 4 will only be executed if if condition becomes false.
"""


