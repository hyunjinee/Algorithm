N=int(input())
L=[*map(int,input().split())]
check=set()
result=0
for i in range(N):
    for j in range(i):
        tmp=L[i]-L[j]
        if tmp in check:
            result+=1
            break
    for j in range(i+1):
        check.add(L[i]+L[j])
print(result)