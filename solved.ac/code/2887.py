"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 행성 터널
description : 최소 신장 트리
"""
import sys
input= sys.stdin.readline

n=int(input())
coord=[]
for i in range(n):
    x,y,z= map(int, input().split())
    coord.append((x,y,z,i))
parent= [i for i in range(n)]
edge=[]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[max(a,b)]=min(a,b)

for i in range(3):
    coord.sort(key=lambda x: x[i])
    for j in range(1,n):
        edge.append((coord[j][3],coord[j-1][3], abs(coord[j][i]-coord[j-1][i])))

edge.sort(key= lambda x: x[2])
answer=0
for x,y,value in edge:
    if find(x)!=find(y):
        answer+=value
        union(x,y)

print(answer)


# import sys
# input = sys.stdin.readline
# n = int(input())
# graph = [[] for _ in range(n+1)]
# c = []
# for i in range(n):
#   x,y,z = map(int, input().split())
#   c.append((x,y,z,i))
# edges = []
# for i in range(3):
#   c.sort(key=lambda x:x[i])
#   for j in range(1, n):
#     edges.append((c[j][3], c[j-1][3], abs(c[j][i]-c[j-1][i])))
# # for i in range(n-1):
# #   for j in range(i+1, n):
# #     x = abs (c[i][0] - c[j][0])
# #     y = abs (c[i][1] - c[j][1])
# #     z = abs (c[i][2] - c[j][2])
# #     # 최단거리, 경로
# #     edges.append((min(x,y,z), i, j))
# edges.sort(key=lambda x:x[2])
# parent = [i for i in range(n+1)]

# def find(x):
#   if parent[x] == x:
#     return x
#   else:
#     return find(parent[x])
# def union(x,y):
#   x = find(x)
#   y = find(y)

#   if x > y:
#     parent[y] = x
#   else:
#     parent[x] = y
# cnt = 0
# ans = 0
# for w,a,b in edges:
#   if find(a) != find(b):
#     union(a,b)
#     cnt += 1
#     ans += w

#   if cnt == n - 1:
#     break

# print(ans)