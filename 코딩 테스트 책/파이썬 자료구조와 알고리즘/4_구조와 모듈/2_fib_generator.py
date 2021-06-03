def fib_generator():
    a, b= 0,1
    while True:
        yield b
        a, b = b , a+b
    

fib  = fib_generator()
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))