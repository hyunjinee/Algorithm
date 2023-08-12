import sys

input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [[0] * (N + 1) for _ in range(N + 1)]

for a in range(N + 1):
    for b in range(N + 1):
        if a == b:
            graph[a][b] = 0
            ans[a][b] = INF

for _ in range(M):
    v1, v2, route = map(int, input().split())
    # 양방향 그래프이므로
    graph[v1][v2] = route
    graph[v2][v1] = route
    # v1 출발 -> v2 도착이면 v1 기준으로 v2가 도착지점이 되어야함.
    ans[v1][v2] = v2
    # 위와 반대
    ans[v2][v1] = v1

# 플로이드 워셜 알고리즘 (점화식 이용 --> DP)
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            # 기존의 a -> b로 가는 저장된 비용보다
            # a -> k -> b로 가는 경로가 더 최단 거리이면
            if graph[a][b] > graph[a][k] + graph[k][b]:
                # 비용을 최단 거리로 갱신
                graph[a][b] = graph[a][k] + graph[k][b]
                # 먼저 들러야하는 지점인 (a, k)의 집하장 값으로 갱신
                ans[a][b] = ans[a][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ans[i][j] == INF:
            print('-', end=' ')
        else:
            print(ans[i][j], end=' ')
    print()