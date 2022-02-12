import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline 

n = int(input())
graph  = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

# [정점 번호][얼리 어답터 체크]
dp = [[0, 0] for _ in range(n + 1)]

def solve_dp(num):
  visited[num] = True
  dp[num][0] = 0
  dp[num][1] = 1 # 자신 포함시키기(얼리어답터 수)

  for i in graph[num]:
    if not visited[i]:
      solve_dp(i)
      dp[num][0] += dp[i][1]
      dp[num][1] += min(dp[i][0], dp[i][1])

solve_dp(1)
print(min(dp[1][0], dp[1][1]))
