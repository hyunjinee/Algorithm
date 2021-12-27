import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
building = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
cost = [0] * (n+1)

for i in range(1, n+1):
  data = list(map(int,input().split()))[:-1]
  cost[i] = data[0]
  pre = data[1:]

  for j in pre:
    building[j].append(i)
    inDegree[i] += 1


result = [0] * (n + 1)
q = deque()
for i in range(1,n+1):
  if inDegree[i] == 0:
    q.append(i)

while q: 
  now = q.popleft()
  result[now] += cost[now]
  for b in building[now]:
    inDegree[b] -= 1
    result[b] = max(result[b], result[now])
    if inDegree[b] == 0:
      q.append(b)

for i in range(1, n+1):
  print(result[i])