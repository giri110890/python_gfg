# python3 code to illustrate the difference between == and is operator

# [] is an empty list
list1 = []
print(id(list1))
list2 = []
print(id(list2))
list3 = list1
print(id(list3))

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2): 
    print("True") 
else: 
    print("False") 


if (list1 is list3): 
    print("True") 
else:     
    print("False")