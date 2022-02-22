
import sys
sys.setrecursionlimit(10**6) 
n, k = map(int, input().split())
numbers = [i for i in range(n+1)]
answer = 0
def dfs(x, kk):
  global answer
  if kk > k :
    return 
  if sum(x) > n :
    return
  if kk == k and sum(x) == n :
    answer += 1
  for i in range(len(numbers)):
    x.append(numbers[i])
    dfs(x, kk+1)
    x.pop()
for i in range(0, n+1):
  dfs([i], 1)
print(answer % 1000000000)