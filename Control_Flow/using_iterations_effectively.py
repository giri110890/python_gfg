# A C-style way of accessing the list elements

cars = ["Aston", "Audi", "McLaren"]
i = 0
while (i < len(cars)):
    print(cars[i])
    i += 1

# Accessing items using for-in loop
for x in cars:
    print(x)

# Accessing items using indexes and for-in
for i in range(len(cars)):
    print(cars[i])

# Eumerate is built-in function that takes input as iterator, 
# list etc and returns a tuple containing index and data at that 
# index in the iterator sequence. For example, enumerate(cars), returns 
# a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), 
# and so on.

# Accessing items using enumerate()
for i, x in enumerate(cars):
    print(x)


# Accessing items and indexes enumerate()
for x in enumerate(cars):
    print(x[0], x[1])

# Enumerate takes parameter start which is default set to zero. We can 
# change this parameter to any value we like. In the below code we have 
# used start as 1.

# demonstrating the use of start in enumerate 
  
cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars, start=1): 
    print (x[0], x[1])

# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"] 
  
# Single dictionary holds prices of cars and  
# its accessories. 
# First three items store prices of cars and 
# next two items store prices of accessories. 
prices = {1:"570000$", 2:"68000$", 3:"450000$", 
          4:"8900$", 5:"4500$"} 
  
# Printing prices of cars 
for index, c in enumerate(cars, start=1): 
    print ("Car: %s Price: %s"%(c, prices[index])) 
  
# Printing prices of accessories 
for index, a in enumerate(accessories,start=1): 
    print ("Accessory: %s Price: %s"
    %(a,prices[index+len(cars)]))

# Python program to demonstrate the working of zip 
  
# Two separate lists 
cars = ["ASton"] 
accessories = ["GPS", "Car Repair Kit",  
               ] 
  
# Combining lists and printing 
for c, a in zip(cars, accessories): 
    print ("Car: %s, Accessory required: %s" %(c, a))

# Python program to demonstrate unzip (reverse  
# of zip)using * with zip function 
  
# Unzip lists 
l1,l2 = zip(*[('Aston', 'GPS'),  
              ('Audi', 'Car Repair'),  
              ('McLaren', 'Dolby sound kit')  
           ]) 
  
# Printing unzipped lists       
print(l1) 
print(l2) 




