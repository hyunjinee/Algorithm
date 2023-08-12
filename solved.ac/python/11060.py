import sys

n = int(input())
jump = list(map(int, sys.stdin.readline().split()))
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
	for j in range(1, jump[i] + 1):
		if i + j < n:
			dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
	print(-1)
else:
	print(dp[n - 1])

# from sys import stdin
# from collections import deque


# def visitable(idx):
#     return idx < n and a[idx] > 0 and not visited[idx]


# def bfs(start):
#     q = deque([start])

#     while q:
#         idx, cnt = q.popleft()
#         if idx + 1 == n:
#             return cnt

#         for i in range(a[idx] + 1):
#             next_idx = idx + i

#             if visitable(next_idx):
#                 visited[next_idx] = True
#                 q.append((next_idx, cnt + 1))
#     return -1


# if __name__ == '__main__':
#     n = int(stdin.readline())
#     a = list(map(int, stdin.readline().split()))
#     visited = [True] + [False] * (n - 1)
#     print(bfs([0, 0]))

	# 

# import sys
# sys.setrecursionlimit(10**9)

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))
# visited = [False] * len(arr)
# cnt = 0
# def dfs(start):
#   global cnt
#   if start == len(arr) - 1:
#     return cnt 

#   cnt += 1


#   for i in range(start, start + arr[start] + 1):
#     visited[start] = True
#     dfs(i)
#     visited[start] = False


# dfs(arr[0])

# print(cnt)