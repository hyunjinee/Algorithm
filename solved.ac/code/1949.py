
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
person = [0] + list(map(int, input().split()))
tree = [[] for i in range(N + 1)]
visit = [False for i in range(N + 1)]
dp = [[0] * 2 for i in range(N + 1)]

def dfs(start):
    visit[start] = True

    for i in tree[start]:
        if not visit[i]:
            dfs(i)
            dp[start][1] += dp[i][0]
            dp[start][0] += max(dp[i][0], dp[i][1])
    dp[start][1] = dp[start][1] + person[start]
        
for i in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
dfs(1)
print(max(dp[1][0], dp[1][1]))
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(20000)
# n = int(input())
# w = [0] + list(map(int, input().split()))
# s = [[] for i in range(n + 1)]
# visit = [False for i in range(n + 1)]
# dp = [[0] * 2 for i in range(n + 1)]
# def dfs(start):
#     visit[start] = True
#     dp[start][0] = w[start]
#     for i in s[start]:
#         if not visit[i]:
#             dfs(i)
#             dp[start][0] += dp[i][1]
#             dp[start][1] += max(dp[i][0], dp[i][1])
# for i in range(n - 1):
#     a, b = map(int, input().split())
#     s[a].append(b)
#     s[b].append(a)
# dfs(1)
# print(max(dp[1][0], dp[1][1]))
# # # n개의 마을 
# # # 1 ~  n

# # # tree


# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # people = [0] +  list(map(int,input().split()))
# # parent= [i for i in range(n+1)]
# # tree = [[] for _ in range(n+1)]
# # for _ in range(n-1):
# #   a,b = map(int,input().split())
# #   tree[a].append(b)
# #   tree[b].append(a)

# # print(tree)



# # def dfs(x):
# #   pass