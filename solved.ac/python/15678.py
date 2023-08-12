from collections import deque
n,d = map(int,input().split())
l = list(map(int,input().split()))
D = deque()
ans = -float('inf')
for i in range(n):
    # print(D)
    # print(ans)
    if D and D[0][1]<i-d: ans = max(ans, D.popleft()[0])
    a = l[i]
    if D and D[0][0]>0: a+=D[0][0]
    while D and D[-1][0]<=a: D.pop()
    D.append((a,i))
print(max(ans,D[0][0]))