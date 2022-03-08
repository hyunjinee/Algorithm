

n,s,m = map(int,input().split())
v = list(map(int, input().split()))
# 곡의 개수 , 시작 볼륨 , 최대 볼륨
dp = [[0] * (m+1 ) for _ in range(n+1)]
dp[0][s] = 1 
for i in range(n):
  for j in range(m+1):
    if dp[i][j] == 1:
      if j + v[i] <= m:
        dp[i+1][j+v[i]] = 1
      if j - v[i] >= 0:
        dp[i+1][j-v[i]] = 1

ans = -1
for i in range(m, -1, -1):
  if dp[n][i] == 1:
    ans = i 
    break
print(ans)


# from collections import deque
# start = deque([s])
# print(start)
# n = n - 1
# cursor = 0
# while start and n >= 0 :
#   l = len(start)
#   for i in range(l):
#     temp  = start.popleft()
#     if 0 <= temp + v[n] <= m :
#       start.append(temp + v[cursor])
#     if 0 <= temp - v[n] <= m:
#       start.append(temp - v[cursor])
#   print(start)
#   n = n - 1
#   cursor += 1
# print(start)