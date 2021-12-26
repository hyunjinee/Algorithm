import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m=map(int,input().split())


parent = [i for i in range(n+1)]


def find (x) :
  if x == parent[x]:
    return x
  else:
    p = find (parent[x])
    parent[x] = p
    return parent[x]

def union(x,y) :
  a =  find(x)
  b = find(y)
  if a  ==b:
    return 

  if a > b :
    parent[a] = b
  else :
    parent[b] = a

for _ in range(m):
  a,b,c = map(int, input().split())

  if a == 0 :
    union(b,c)
  else:
    if find(b) == find(c) :
      print("YES")
    else :
      print("NO")
