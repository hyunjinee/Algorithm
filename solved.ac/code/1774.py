import sys
input = sys.stdin.readline
n,m = map(int,input().split())

coordinations = [list(map(int,input().split())) for _  in range(n)]
graph =[ ]
parent = [i for i in range(n)]
def union (a,b ):
  a, b = find(a), find(b)
  parent[max(a,b)] = min(a,b)

def find(a):
  if parent[a] == a: 
    return a
  parent[a] = find(parent[a])
  return parent[a]

def check(a,b) :
  return find(a) == find(b)
def dist(a,b):
  return ((a[0]- b[0]) ** 2  + (a[1]- b[1]) ** 2) ** 0.5

for _ in range(m):
  x, y = map(int,input().split())
  union(x-1, y-1)
for i in range(n-1):
  for j in range(i+1, n):
    graph.append((i, j, dist(coordinations[i], coordinations[j])))
graph.sort(key= lambda x: x[2])
answer = 0 
for i in graph:
  if not check(i[0], i[1]):
    union(i[0], i[1])
    answer += i[2]
  
print("%.2f" %(answer))