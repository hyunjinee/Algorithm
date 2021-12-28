import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)

heap = []
result = []
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  inDegree[b] += 1

for i in range(1, n+1):
  if inDegree[i] == 0:
    heapq.heappush(heap, i)
while heap:
  data=  heapq.heappop(heap)
  result.append(data)
  for v in graph[data]:

    inDegree[v] -= 1
    if inDegree[v] == 0 : 
      heapq.heappush(heap, v)



print(*result)