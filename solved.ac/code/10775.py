# 공항에는 G개의 게이트가 있다.
# P개의 비행기가 도착할 예정이며,

import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
planes = []
answer  =0 
for _ in range(p):
  planes.append(int(input()))
def union (x, y):
  x = find(x)
  y = find(y)
  parent[y] =  x
def find (x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]
parent = [i for i in range(g+1)]
for plane in planes:
  p = find (plane)
  if p == 0 :
    break
  answer += 1
  union(p-1, p)
# print(parent)
print(answer)





# cnt = 0
# for i in plane:
#   x = find(i)
#   union(x, x-1)
#   cnt += 1
# print(cnt)
