import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# n가수의 수 m은 보조 피디의 수
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
for i in range(m):
  lst = list(map(int ,input().split()))
  for s in range(1, lst[0]):
    graph[lst[s]].append(lst[s+1])
    inDegree[lst[s+1]] += 1

q = deque()
ans = []
for i in range(1, n+1):
  if inDegree[i] == 0:
    q.append(i)

while q:
  cur = q.popleft()
  ans.append(cur)

  for i in graph[cur]:
    inDegree[i] -= 1
    if inDegree[i] == 0:
      q.append(i)

if len(ans ) != n:
  print(0)
else:
  for i in ans:
    print(i)