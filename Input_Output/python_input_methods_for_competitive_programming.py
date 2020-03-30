# basic method of input output
# inout N
n = int(input())

# input the array
arr = [int(x) for x in input().split()]

# initialize variable
summation = 0

# calculate sum
for x in arr:
    summation += x

# print answer
print(summation)

# import inbuild standar input output
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed
def main():
    # input via readline method
    n = stdin.readline()

    # array input similar method
    arr = [int(x) for x in stdin.readline().split()]

    # intialize the variable
    summation = 0

    # calculate sum
    for x in arr:
        summation += x
    
    # print answer via write
    # write method writes only
    # string operations
    # so we need to convert any
    # data into string for input
    stdout.write(str(summation))

# call the main method
if __name__ == "__main__":
    main()

# template begins
###############################

# import libraries for input/ output handling
# on generic level
import atexit, io, sys

# A stream implementation using an in-memory bytes
# buffer. It inherits BufferedIOBase
buffer = io.BytesIO()
sys.stdout = buffer

# print via here
@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())

################################3
# template ends

# normal method followed
# input N 
n = int(input()) 
  
# input the array 
arr = [int(x) for x in input().split()] 
  
# initialize variable 
summation = 0
  
# calculate sum 
for x in arr: 
    summation += x 
  
# print answer 
print(summation) 