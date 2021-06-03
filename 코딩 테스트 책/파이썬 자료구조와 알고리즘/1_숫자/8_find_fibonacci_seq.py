import math

def find_fibonacci_swq_iter(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def find_fibonacci_swq_rec(n):
    if n < 2 : return n
    return find_fibonacci_swq_rec(n-1) + find_fibonacci_swq_rec(n-2)

def find_fibonacci_swq_form(n):
    sq5 = math.sqrt(5)
    phi = (1+ sq5) /2
    return  int(math.floor(phi ** n / sq5))
