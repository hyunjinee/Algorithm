for i in range(3):
    N = int(input())
    count = 0
    for _ in range(N):
        a = int(input())
        count += a
    if(count ==0): 
        print(0)
    elif(count >0):
        print("+")
    else:
        print("-")