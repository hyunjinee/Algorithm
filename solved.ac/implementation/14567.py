import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# n 과목 수  m은 선수 조건의 수

def topology_sort():
  q = deque()
  for i in range(n):
    if indegree[i] == 0:
      q.append(i)  
  while q:
    now = q.popleft()
    for i in graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0:
        result[i] = result[now] + 1

        q.append(i)

  print(*result)

indegree = [0] * n
result = [1] * n

graph = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  indegree[b - 1] += 1

topology_sort()