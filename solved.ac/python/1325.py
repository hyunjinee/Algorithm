import sys
from collections import deque, defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())

arr = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    arr[e].append(s)


def bfs(x):
    visited = [False] * (N+1)
    visited[x] = True

    queue = deque([x])
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt


_max = 0
answer = []
for i in range(1, N+1):
    result = bfs(i)
    if result > _max:
        _max = result
        answer = [i]
    elif result == _max:
        answer.append(i)

print(*answer)
# print(arr)
# graph = [[0] * (N + 1) for _ in range(N + 1)]

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# connected_component = [0] * (N + 1)


# print(graph)
# for i in range(1, N+1):
#     :

# 그래프를 그리고

# union find
# #
# parent = [i for i in range(N+1)]

# val = [0] * (N+1)
# cnt = 0

# def find(x):
#     global cnt
#     cnt += 1
#     if x == parent[x]:
#         val[x] = cnt
#         cnt = 0
#         return x
#     else:
#         p = find(parent[x])
#         parent[x] = p
#         return p

# def union(x, y):

#     a = find(x)
#     b = find(y)
#     if a != b:

#         if a > b:
#             parent[b] = a
#         else:
#             parent[a] = b

# for i in range(M):
#     a, b = map(int, input().split())
#     union(a, b)

# print(parent)
# print(val)
