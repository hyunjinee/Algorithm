T = int(input())
countzero=0
countone=0






def fib(n):
    global countzero
    global countone
    if n==0:
        countzero+=1
        return 0
    if n==1:
        countone+=1
        return 1

    else:
        return  fib(n-1) + fib(n-2)

for i in range(T):
    a = int(input())
    fib(a)
    print(countzero, countone)
    countzero = 0
    countone = 0
