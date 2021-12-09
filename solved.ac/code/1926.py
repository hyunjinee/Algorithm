"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 그림
description : graph
"""
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    images[i][j] = 0
    size = 1  # 최초 들어갈 때 그림 크기 1로 시작
    while q:
        x, y = q.popleft()
        for k in range(4):  # 상하좌우 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 인덱스 범위안에 있고
                if images[nx][ny]:  # 주변이 연결된 그림이면
                    q.append((nx, ny))
                    size += 1
                    images[nx][ny] = 0
    else:
        size_list.append(size)
        return


if __name__ == "__main__":
    n, m = map(int, input().split())
    images = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0  # 그림의 수
    size_list = []  # 그림의 크기들
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if images[i][j]:  # 한번 들어갈 때마다 그림 +1
                bfs(i, j)
                cnt += 1

    print(cnt)
    print(max(size_list) if size_list else 0)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n, m = map(int, input().split())

# paint = [list(map(int, input().split())) for _ in range(n)]

# d = [(0,1), (0,-1), (1,0), (-1,0)]

# def dfs (y, x ) :
#   paint[y][x] = 0
#   ans = 1
#   for dy, dx in d:
#     ny, nx = y + dy, x + dx
#     if 0 <= ny < n and 0 <= nx < m and paint[ny][nx] == 1:
#       ans += dfs(ny, nx)
#   return ans

# res = []
# count = 0
# for i in range(n):
#   for j in range(m):
#     if paint[i][j] == 1:
#       count += 1

#       res.append(dfs(i,j))

  
# print(count)
# print(max(res))