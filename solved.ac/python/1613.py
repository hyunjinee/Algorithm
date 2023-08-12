"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 역사
description : graph, floyd-warshall
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]
for _ in range(m):
  x, y = map(int, input().split())
  a[x-1][y-1] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      if a[i][k] and a[k][j] :
        a[i][j] = 1
s = int(input())
for _ in range(s):
  x, y = map(int, input().split())
  if a[x-1][y-1] == 1:
    print(-1)
  elif a[y-1][x-1] == 1:
    print(1)
  elif a[x-1][y-1] == 0:
    print(0)
# sagun = [list(map(int, input().split())) for _ in range(k)]

# parent = [i for i in range(n+1)]

# def find(x):
#   if x != parent[x]:
#     parent[x] = find(parent[x])
#   return parent[x]

# def union(x,y ):
#   if x > y : 
#     parent[x] = y
#   else: 
#     parent[y] = x

# def find_up (x):
#   return parent[x]

# def find_before(a, b):
#     keep = parent[b]
#     while True:
#       if keep == a:
#         print(-1)
#         break
#       else: 
#         keep = find_up(keep)
#         print(keep)



# for a, b in sagun:
  
#   union(find(a), find(b))


# s = int(input())
# for _ in range(s):
#   a, b = map(int, input().split())
#   # 앞에 있는 번호의 사건이 먼저 일어났으면 -1
#   # 뒤에있는 번호의 사건이 먼저 일어났으면 1
#   # 유추할 수 없으면 0
#   if find(a) != find(b):
#     print(0)
#     print(parent)
#   else:
    
#     pass