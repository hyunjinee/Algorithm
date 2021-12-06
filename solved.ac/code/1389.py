import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):
    num = [0] * (N+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                num[i] = num[a] + 1
                q.append(i)


result = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    result.append(bfs(graph, i))
