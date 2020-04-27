# Nested functions in Python
# A function which is defined inside another function is known as nested
# function. Nested functions are able to access variables of the 
# enclosing scope.

# Python program to illustrate nested functions
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)
    
    innerFunction()

if __name__ == "__main__":
    outerFunction("Hey! ")

# Python program to illustrate closures
def outerFunction1(text):
    text = text

    def innerFunction1():
        print(text)
    
    # Note we are returning function Without parathesis
    return innerFunction1

if __name__ == '__main__':
    myFunction = outerFunction1("giii ")
    myFunction()

# As observed from above code, closures help to invoke function outside 
# their scope.
# The function innerFunction has its scope only inside the outerFunction. 
# But with the use of closures we can easily extend its scope to invoke a 
# function outside its scope.

# Python program to illustrate closures
import logging
logging.basicConfig(filename='example.log', level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,
            args))
        print(func(*args))
    # NEcessary for closure to work (returning without parenthesis)
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
                    