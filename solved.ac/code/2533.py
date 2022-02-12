import sys
input =sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())

edges = [{} for i in range(N + 1)]
for i in range(N-1):
	u,v = map(int, input().split())
	edges[u][v] = 1
	edges[v][u] = 1

visited = [0] * (N + 1)
result = 0

findings = [1]

def dfs(cur):
	visited[cur] = 1
	val = [0,1]
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		child_val = dfs(nxt)
		val[1] += min(child_val[1],child_val[0])
		val[0] += child_val[1]
	return val

print(min(dfs(1)))


# # 얼리 어답터의 수.

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


# n = int(input()) # vertex

# tree = [[] for _ in range(n + 1)]
# visited = [ 0 for _ in range(n + 1)]
# dp = [[0,0] for _ in range(n + 1)]

# for _ in range(n - 1):
#   u, v = map(int , input().split())
#   tree[u].append(v)
#   tree[v].append(u)

# def dfs(r):
#   visited[r] = 1
#   dp[r][0] = 1
#   for i in tree[r]:
#     if not visited[i]:
#       dfs(i)
#       dp[r][0] += min(dp[i][0], dp[i][1])
#       dp[r][1] += dp[i][0]

# dfs(1)

# print(min(dp[1][0], dp[1][1]))

