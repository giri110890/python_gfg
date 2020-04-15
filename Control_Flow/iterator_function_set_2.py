# Python code to demonstrate the working of  
# islice() and starmap()

# importing "itertools" for iterator operations 
import itertools
import iterators

# initializing list  
li = [2, 4, 5, 7, 8, 10, 20] 

# initializing tuple list 
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]

# using islice() to slice the list acc. to need 
# starts printing from 2nd index till 6th skipping 2 
print ("The sliced list values are : ",end="") 
print (list(itertools.islice(li, 1, 6, 2))) 

# using starmap() for selection value acc. to function 
# selects min of all tuple values 
print ("The values acc. to function are : ",end="") 
print (list(itertools.starmap(min,li1)))

# initializing list  
li = [2, 4, 6, 7, 8, 10, 20] 
  
# storing list in iterator 
iti = iter(li) 
  
# using takewhile() to print values till condition is false. 
print ("The list values till 1st false value are : ",end="") 
print (list(itertools.takewhile(lambda x : x%2==0,li ))) 
  
# using tee() to make a list of iterators 
# makes list of 3 iterators having same values. 
it = itertools.tee(iti, 4) 
  
# printing the values of iterators 
print ("The iterators are : ") 
for i in range (0,4): 
    print (list(it[i]))

# using zip_longest() to combine two iterables. 
print ("The combined values of iterables is  : ") 
print (*(itertools.zip_longest('G','ekfrek',fillvalue='_' ))) 

# using product() to print the cartesian product 
print ("The cartesian product of the containers is : ") 
print (list(itertools.product('AB','12')))


# using permutations to compute all possible permutations 
print ("All the permutations of the given container is : ") 
print (list(itertools.permutations('GfG',2)))

# using combinations() to print every combination 
# (without replacement) 
print ("All the combination of container in sorted order(without replacement) is : ") 
print (list(itertools.combinations('1234',2)))

# using combinations_with_replacement() to print every combination 
# with replacement 
print ("All the combination of container in sorted order(with replacement) is : ") 
print (list(itertools.combinations_with_replacement('GfG',2)))

# using repeat() to repeatedly print number 
print ("Printing the numbers repeatedly : ") 
print (list(itertools.repeat(25,4))) 