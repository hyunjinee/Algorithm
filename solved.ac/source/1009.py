import sys
c = []
count = int(sys.stdin.readline())
for _ in range(count):
    a, b =  map(int,sys.stdin.readline().split())
    work = (a**b)%10
    c.append(work)
    
for i in c:
    print(i)