import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = []

def dfs(depth):
  if depth == m:
    print(*s)

    return 
  for i in range(n):
    s.append(nums[i])
    dfs(depth+1)
    s.pop()

dfs(0)

