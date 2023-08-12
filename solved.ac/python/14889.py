import sys
input = sys.stdin.readline
def dfs(idx, cnt):
  global ans
  if cnt == n// 2:
    start, link = 0, 0
    for i in range(n):
      for j in range(n):
        if select[i] and select[j]:
          start += a[i][j]
        elif not select[i] and not select[j]:
          link += a[i][j]
    ans = min(ans, abs(start - link))
  for i in range(idx,n ):
    if select[i]:
      continue
    select[i] = 1
    dfs(i+1, cnt+1)
    select[i] = 0
n = int(input())
a = [list(map(int ,input().split())) for _ in range(n)]
select = [ 0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)