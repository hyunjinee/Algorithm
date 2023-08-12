import sys; input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key = lambda x: x[1], reverse=True)

ans = time[0][1] - time[0][0]

for i in range(1, n):
  if ans > time[i][1]:
    ans = time[i][1] - time[i][0]
  else: 
    ans -= time[i][0]

print(ans) if ans >= 0 else print(-1)