import sys
input = sys.stdin.readline

# v ,e 

n =int(input())
weights = [0] + list(map(int,input().split()))
lines = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int,input().split())
  lines[a].append(b)
  lines[b].append(a)
visited = [0] * (n + 1)
dp = [[0,0] for _ in range(n+1)]
def dfs(start):
  visited [start] = 1
  dp[start][0] = weights[start]
