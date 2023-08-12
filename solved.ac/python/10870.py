n = int(input())


lst = [0,1]


def fibo(n):
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return
    else:


        for i in range(n-1):
            lst.append(lst[-1] + lst[-2])

        
    print(lst[-1])
            

fibo(n)