# 방향이 없는 그래프가 주어진다. 연결 요소의 개수를 구하는 프로그램을 작성해라


# 입력으로는 정점의 개수 n 과 간선의 개수 m 이 주어진다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n+1)
group = 0

def bfs(init):
    global visited
    stack = [init]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v]  = 1
            for g in graph[v]:
                if not visited[g]:
                    stack.append(g)


for i in range(1, n+1):
    if not visited[i]:
        group += 1
        bfs(i)




print(group)