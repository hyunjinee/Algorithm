"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 도시 분할 계획
description : mst
"""
import sys

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
def union(x,y):
  a = find(x)
  b = find(y)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

input = sys.stdin.readline
n, m = map(int,input().split())

graph = []
for _ in range(m):
  a,b,c = map(int,input().split())
  graph.append([c,a,b])

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

graph.sort()
selected = []

answer = 0
for c, a, b in graph:
  if find(a) != find(b):
    union(a,b)
    answer += c
    selected.append(c)

answer -= selected.pop()

print(answer)