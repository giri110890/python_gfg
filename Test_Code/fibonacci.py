def two(f = None): return 2 if not f else f(2)
def four(f = None): return 4 if not f else f(4)

def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x + y
def times(y): return lambda x: x * y
def divided(y): return lambda x: x // y
print(seven(times(five())))
print(six(divided(two())))




