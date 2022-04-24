import sys;input=sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
def dfs(depth):
  if depth == n:
    result.append(sum(abs(explore[i] - explore[i + 1]) for i in range(n-1)) )
  for i in range(n):
    if visited[i]:
      continue
    explore.append(arr[i])
    visited[i] = 1
    dfs(depth + 1)
    visited[i] = 0
    explore.pop()
visited = [0] * n
result, explore = [], []
dfs(0)
print(max(result))
# import sys
# from itertools import permutations

# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))

# cases = list(permutations(a))

# answer = 0
# for case in cases:
#     mid_sum = 0
#     for i in range(n - 1):
#         mid_sum += abs(case[i] - case[i + 1])
#     answer = max(mid_sum, answer)

# print(answer)