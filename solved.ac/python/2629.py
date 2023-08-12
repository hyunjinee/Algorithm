import sys;input=sys.stdin.readline
n = int(input())
weights = list(map(int,input().split()))
k = int(input())
marbles = list(map(int,input().split()))
dp = [[0 for _ in range(15001)] for _ in range(n+1)]
possible = []

def dfs(weights, n, now, left, right):
  new = abs(left - right)
  
  if new not in possible: 
    possible.append(new)
  
  if now == n : return 0

  if dp[now][new] == 0:
    dfs(weights, n, now + 1, left + weights[now], right)
    dfs(weights, n, now + 1, left, right + weights[now])
    dfs(weights, n, now+1, left, right)
    dp[now][new] = 1
dfs(weights, n, 0, 0, 0)
for i in range(0, k):
  if marbles[i] in possible:
    print("Y" , end = " ")
  else:
    print("N", end = " ")
# def scale (weight, n, now, left, right) :
#   new = abs(left - right)
#   if new not in possible:
#     possible .append(new)
#   if now  == n:
#     return 0
#   if ans[now][new] == 0:
#     scale(weight, n, now + 1, left + weight[now], right)
#     scale(weight, n, now + 1, left, right + weight[now])
#     scale(weight, n, now + 1, left, right)
#     ans[now][new] = 1

# scale(weights,n,0,0,0)
# for i in marbles:
#   if i in possible:
#     print('Y', end=' ')
#   else:
#     print('N', end=' ')