import sys
input=sys.stdin.readline
N = int(input())
parents = [0]+list(range(1, N+1))
visited = [[0]*1001 for _ in range(1001)]

def find(n):
    if parents[n] == n:
        return n
    parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    parents[fa] = fb

for n in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        if visited[x][y1]:
            union(visited[x][y1], n)
        visited[x][y1] = n
        if visited[x][y2]:
            union(visited[x][y2], n)
        visited[x][y2] = n
        
    for y in range(y1, y2+1):
        if visited[x1][y]:
            union(visited[x1][y], n)
        visited[x1][y] = n
        if visited[x2][y]:
            union(visited[x2][y], n)
        visited[x2][y] = n
    
cnt = len(set(find(i) for i in range(1, N+1))) - 1
if not visited[0][0]:
    cnt += 1

print(cnt)
# import sys
# sys.setrecursionlimit(10**6)
# N = int(input())
# lined = {(0, 0)}
# for _ in range(N):
#     x1, y1, x2, y2 = map(int, input().split())
#     x1, x2, y1, y2 = *sorted([x1*2, x2*2]), *sorted([y1*2, y2*2])
#     for x in range(x1, x2+1):
#         lined.add((x, y1))
#         lined.add((x, y2))
#     for y in range(y1, y2+1):
#         lined.add((x1, y))
#         lined.add((x2, y))

# dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
# def dfs(x, y):
#     if (x, y) in lined:
#         lined.remove((x, y))
#     else:
#         return
    
#     for v in range(4):
#         nx, ny = x+dx[v], y+dy[v]
#         if not all([-1000<=nx<=1000, -1000<=ny<=1000]):
#             continue
#         dfs(nx, ny)
        
# cnt = -1
# while lined:
#     cnt += 1
#     dfs(*next(iter(lined)))

# print(cnt)

# # import sys
# # from collections import deque
# # input = sys.stdin.readline
# # n = int (input())
# # dx = [1,-1,0,0]
# # dy = [0, 0, 1, -1]

# # a = [[0] * 2001 for _ in range(2001)]
# # c = [[0] * 2001 for _ in range(2001)]
# # start = []
# # for _ in range(n):
# #   x1,y1 ,x2, y2 = map(int ,input().split())
# #   x1 += 500; y1 += 500; x2 += 500; y2 += 500
# #   x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2