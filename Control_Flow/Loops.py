# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")

'''
If else like this:
if condition: 
    # execute these statements 
else: 
    # execute these statements 

'''

'''
and while loop like this are similar

while condition: 
     # execute these statements 
else: 
     # execute these statements 

'''

# Python program to illustrate combining else with while
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

'''
Syntax for loop

for iterator_var in sequence:
    statements(s)

'''

# Python program to illustrate Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i)

# Iterating over a String 
print("\nString Iteration")     
s = "Geeks"
for i in s : 
    print(i)

# Iterating over dictionary 
print("\nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s  %d" %(i, d[i]))

# Python program to illustrate 
# Iterating by index 
  
list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
    print (list[index])

# Python program to illustrate 
# combining else with for 
  
list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
    print (list[index]) 
else: 
    print ("Inside Else Block")


for i in range(1, 5): 
    for j in range(i): 
         print(i, end=' ') 
    print()

# Prints all letters except 'e' and 's'
# Continue Statement: It returns the control to the beginning of the loop.
for letter in 'geeksforgeeks':
    if letter == "e" or letter == "s":
        continue
    print ('Current Letter : ', letter)

# Break Statement: It brings control out of the loop
for letter in 'geeksforgeeks':  
  
    # break the loop as soon it sees 'e'  
    # or 's' 
    if letter == 'e' or letter == 's': 
         break
  
print ('Current Letter :', letter)

# We use pass statement to write empty loops.PAss is also used for empty
# control statement, function and classes

# An empty loop
for letter in "geeksforgeeks" :
    pass
print("Last Letter: ", letter)
