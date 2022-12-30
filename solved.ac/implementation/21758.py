n = int(input())
m = list(map(int, input().split()))
target = sum(m[:])
ans = 0
temp = m[0]
for i in range(1,n):
  temp += m[i]
  ans = max(ans, target - m[0] + target - temp - m[i])
m.reverse()
temp = m[0]
for i in range(1,n):
  temp += m[i]
  ans = max(ans, target - m[0] + target - temp - m[i])
for i in range(1, n):
  ans = max(ans , target- m[0] - m[-1] + m[i])
print(ans)