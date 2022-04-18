import sys;input=sys.stdin.readline
n = int(input()) # 후보의 수
s = [int(input()) for _ in range(n)]
ans = 0
while True:
  _max = max(s)
  _idx = s.index(_max)
  _count = s.count(_max)

  if _count > 1 and _idx == 0:
    ans += 1
    break

  if _idx == 0 :
    break
  
  s[_idx] -= 1
  s[0] += 1
  ans += 1

print(ans)