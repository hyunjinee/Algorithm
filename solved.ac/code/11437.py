import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)
d =[0] * (n+1) # 각 노드 까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는가?

for _ in range(n-1):
  a,b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

def dfs(x, depth):
  c[x] = True
  d[x] = depth
  for y in tree[x]:
    if c[y]:
      continue
    parent[y] = x
    dfs(y, depth + 1)
def lca(a, b) :
  while d[a] != d[b]:
    if d[a] > d[b]:
      a = parent[a]
    else:
      b = parent[b]
  while a != b:
    a = parent[a]
    b = parent[b]
  return a

dfs(1,0)
m = int(input())
for _ in range(m):
  x,y = map(int,input().split())
  print(lca(x,y))


