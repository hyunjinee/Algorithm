

n = int(input())
a = list(map(int, input().split()))
increase = [1 for _ in range(n)]
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      increase[i] = max(increase[i], increase[j]+1 )
# print(increase)
decrease = [1 for _ in range(n)]

for i in range(n-1, -1, -1):
  for j in range(n-1, i, -1):
    if a[i] > a[j]:
      decrease[i] = max(decrease[j]+ 1, decrease[i])
# print(decrease)

result = [0 for _ in range(n)]
for i in range(n):
  result[i] = increase[i] + decrease[i] - 1

print(max(result))
# for i in range ( 1, n ):
#   dp = [1 for _ in range(n)]
#   s1 = []
#   for j in range(i):
#     if a[i] > a[j]:
#       s1.append(dp[j])
#       # dp[i] += 1
#   dp[i] += max(s1)
#   print(dp, "first")
#   s = []
#   for k in range(i+1, n):
#     if a[k] < a[i]:
#       # dp[i] += 1
#       s.append(dp[k])

#   print(dp, "Second")
#   dp[i] += max(s)
#   print(s, "흠~")
#   break