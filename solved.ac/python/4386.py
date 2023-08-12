# 결국 최소 신장 트리 문제입니다.
import sys
import math
input = sys.stdin.readline
n = int(input())
location = []
edges = []
for _ in range(n):
  x, y = map(float, input().split())
  location.append((x, y))
for i in range(n-1):
  for j in range(i, n):
    if i == j :
      continue
    distance = round(math.sqrt((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2),2)
    edges.append((distance, i, j))
    edges.append((distance, j, i))
edges.sort(key=lambda x: x[0])
parent = list(range(n+1))

def union(a,b):
  a = find (a)
  b = find (b)

  if b < a : 
    parent[a] = b
  else :
    parent[b] = a
def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]


sum = 0
for w, a, b in edges:
  if find(a) != find(b):
    union(a,b)
    sum += w

print(sum)