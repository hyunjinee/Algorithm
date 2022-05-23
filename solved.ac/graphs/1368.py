import sys

input = sys.stdin.readline

n = int(input())
w = [int(input()) for _ in range(n)]
p = [int(i) for i in range(n+1)]
edges = []

def find(n):
  if p[n] == n:
    return n
  else:
    p[n] = find(p[n])
    return p[n]

def union(x, y):
  x = find(x)
  y = find(y)

  if x != y:
    p[y] = x

for i in range(n):
  weight = list(map(int, input().split()))
  for j in range(n):
    if weight[j]:
      edges.append([i, j, weight[j]])
for i in range(n):
  edges.append([i, n, w[i]])
edges.sort(key=lambda x: x[2])

cnt = 0
cost = 0

while edges: 
  a, b ,w = edges.pop(0)
  if find(a) == find(b):
    continue
  union(a,b)
  cost += w

print(cost)
