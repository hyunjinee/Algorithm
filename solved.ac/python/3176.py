import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

queue = deque([(1,1)])
depth = [0] * (n + 1 )

while queue:
  i, d = queue.popleft()
  for j, w in graph[i]:
    if not depth[j]:
      queue.append((j, d+ 1))
      depth[j] = d + 1 
      dp[j][0] = [ i, w, w]


k = int(input())

for _ in range(k):
  d, e = map(int, input().split())
  # d,e 연결에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 구해서 출력

  