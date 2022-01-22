import sys
input = sys.stdin.readline

t = int(input())

def find(x):
  if parent[x] == x:
    return x
  else:
    root_x = find(parent[x])
    parent[x] = root_x
    return parent[x]
def union(a,b):
  a = find(a)
  b = find(b)

  if a != b:
    parent[b] = a
    number[a] += number[b]


for _ in range(t):
  f = int(input())
  parent = {}
  number = {}

  for _ in range(f):
    x, y = input().rstrip().split(" ")
    if x not in parent:
      parent[x] = x
      number[x] = 1
    if y not in parent:
      parent[y] = y
      number[y] = 1
    
    union(x,y)
    print(number[find(x)])