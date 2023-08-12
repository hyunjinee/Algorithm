N = int(input())
list1=[]

for _ in range(N):
    a, b = map(int,input().split())
    list1.append(b-a)
list1.sort()
if len(list1)%2 != 0:
    print(1)
else:
    k = len(list1)//2
    print(list1[k]-list1[k-1]+1)