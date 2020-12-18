import sys
c = []
count = int(sys.stdin.readline())
for _ in range(count):
    a, b =  map(int,sys.stdin.readline().split())
    if(a ==1):
        work = 1
    elif(a==5):
        work= 5
    elif(a==6):
        work = 6
    elif(a==4 or a==9):
        b=b%2
        if(b==1):
            work = a
        else:
            work = (a*a)%10
    else:
        work = (a**b)%10
    c.append(work)
    
for i in c:
    print(i)