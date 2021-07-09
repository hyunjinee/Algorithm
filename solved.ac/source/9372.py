# # # # n개의 국가를 여행하면서 자아를 찾는 상근이
# # # # 최대한 적은 종류의 비행기를 타고 국가를이동
# # # # 비행스케줄이 주어 졌을 때 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행


# # # # 상근이가 한국가에서 다른 국가로 이동할 때 다른국가(방문한 국가 거쳐가도ㅗ딘다.)
# # # import sys 
# # # input = lambda: sys.stdin.readline().strip()

# # # t = int(input())

# # # # 첫번째 줄에는 국가의 수 

# # # for i in range(t):
# # #     n, m = map(int, input().split())

# # #     # 새로운 비행기를 무서워해.
# # #     root = [[0] * n for _ in range(n)]

# # #     count = 0
# # #     # 1 2 2 3 1 3
# # #     for j in range(m) :
# # #         a, b = map(int, input().split())
# # #     root[a][b] = 1
# # #     root[b][a] = 1
        

# # # # 첫번째 줄에는 국가의 수와 비행기의 종류 M


# # import sys
# # t = int(sys.stdin.readline())
# # for i in range(t):
# #     n, m = map(int, sys.stdin.readline().split())
# #     for j in range(m):
# #         a, b = map(int, sys.stdin.readline().split())
# #     print(n - 1)


# import sys

# def dfs(node, cnt):
#     check[node] = 1
#     for n in graph[node]:
#         if check[n] == 0:
#             cnt = dfs(n, cnt+1)
#     return cnt

# for _ in range(int(sys.stdin.readline())):
#     N, M = map(int, sys.stdin.readline().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         u, v = map(int, sys.stdin.readline().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     check = [0]*(N+1)
#     check[1] = 0
#     cnt = dfs(1, 0)
#     print(cnt)


from collections import deque
import sys

input =sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    c[x] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                c[nx] = 1
                cnt += 1
                q.append(nx)
    return cnt 

tc  = int(input())
# 입력받아 테스트케이스
while tc:
    n, m = map(int, input().split())
    a = [ [] for _ in range(n)]
    c = [0 for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        a[x-1].append(y-1)
        a[y-1].append(x-1)
    ans = 0
    for i in range(n):
        if c[i] == 0:
            ans += bfs(i)

    print(ans)

    tc -= 1