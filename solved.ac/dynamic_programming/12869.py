n = int(input())
lst = list(map(int, input().split()))
import itertools

dp = [[ [-1 for _ in range(61)] for _ in range(61)] for _ in range(61) ]

def go(a,b,c):
  if a < 0:
    return go(0,b,c)
  if b < 0:
    return go(a,0,c)
  if c < 0:
    return go(a,b,0)

  if a == 0 and b == 0 and c == 0:
    return 0

  if dp[a][b][c] != -1:
    return dp[a][b][c]

  dp[a][b][c] = 99999999

  for case in list(itertools.permutations([1,3,9])):
    dp[a][b][c] = min(dp[a][b][c], go(a-case[0], b-case[1], c-case[2]))
  dp[a][b][c] += 1
  return dp[a][b][c]

scv = [0,0,0]
for i in range(len(lst)):
  scv[i] = lst[i]
print(go(scv[0], scv[1], scv[2]))
