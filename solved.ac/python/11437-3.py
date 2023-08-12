from collections import defaultdict
import sys
from functools import cache
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

depth, parent = [-1] * (n + 1), [-1] * (n + 1)
depth[1] , parent[1] = 0, 1
def dfs(x, d):
  depth[x] = d
  for y in graph[x]:
    if depth[y] == -1:
      parent[y] = x
      depth[y] = d
      dfs(y, d + 1)
@cache
def lca(x,y):
  if depth[x] > depth[y]: x, y = y, x
  while depth[x] < depth[y] : y = parent[y]
  while x != y: x, y = parent[x], parent[y]
  return x

dfs(1, 0)

for _ in range(int(input())):
  a, b = map(int,input().split())
  print(lca(a,b))
