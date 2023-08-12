n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
  s = []
  for j in range(i):
    if a[i] < a[j]:
      s.append(dp[j])
  if not s:
    continue
  else:
    dp[i] += max(s)
print(max(dp))