import sys; input = sys.stdin.readline
n = int(input())
c = [int(input()) for _ in range(n)]
c.sort(reverse=True)
ans = 0
for i in range(0, n, 3):
  if i + 2 >= len(c):
    left = i
    break 
  ans += sum(c[i: i + 2])

try:
  ans += sum(c[left:])
except:
  pass


print(ans)