# 방향 그래프가 주어졌을 때  그 그래프를 SCC로 나누어라.

"""
강한 결합 요소란 그래프 안에서 강하게 결합된 정점 집합을 의미합니다. 서로 긴밀하게 연결되어 있다고 하여 
강한 결합 요소라고 말합니다. 같은 SCC에 속하는 두 정점은 서로 도달이 가능하다라는 특징이 있습니다.
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
reverse_graph = [[] for _ in range(v+1)]
for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  reverse_graph[b].append(a)


def dfs(node, visit, stack):
  visit[node] = 1
  for now in graph[node]:
    if visit[now] == 0:
      dfs(now, visit, stack)
  stack.append(node)

def reverse_dfs(node, visit, stack):
  visit[node] = 1
  stack.append(node)
  for now in reverse_graph[node]:
    if visit[now] == 0:
      reverse_dfs(now, visit, stack)

stack = []
visit = [0]*(v+1)
for i in range(1, v+1):
  if visit[i] == 0 :
    dfs(i, visit, stack)
visit = [0] * (v+1)
result = []


while stack :
  scc = []
  node = stack.pop()
  if visit[node] == 0 :
    reverse_dfs(node, visit, scc)
    result.append(sorted(scc))
  


print(len(result))
answer = sorted(result)
for i in answer:
    print(*i, -1)