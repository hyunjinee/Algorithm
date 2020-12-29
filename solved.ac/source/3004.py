N = int(input())


if N%2==0:

    
    print(((N//2)+1)**2)

elif N%2==1:
    N=N//2
    
    print((N+1)*(N+2))