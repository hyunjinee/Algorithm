import sys
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l, r = 0, 10 ** 16
  while l <= r:
    mid = (l + r) // 2
    now = mid * (mid + 1) // 2
    if now <= n:
      l = mid + 1
    else :
      r = mid - 1

  print(r)