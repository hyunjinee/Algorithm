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
    else:
        work = (a**b)%10
    c.append(work)
    
for i in c:
    print(i)