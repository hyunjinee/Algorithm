import sys; input = sys.stdin.readline
n = int (input())
arr = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
edges = []
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(0, n):
    for j in range(i):
      edges.append((arr[i][j], i, j))

edges.sort()
answer = 0 
for cost, a, b in edges:
  if find_parent(parent, a) != find_parent(parent, b):
    union(parent, a, b)
    answer += cost

print(answer)