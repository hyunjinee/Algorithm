import sys; input = sys.stdin.readline
n = int(input())
lines = list(tuple(map(int, input().split())) for _ in range(n))
lines.sort()
start = lines[0][0]
end = lines[0][1]

ans = 0 

for k in range(1, n):
  now_start, now_end = lines[k]

  if end > now_start:
    end = max(end, now_end)
  
  else:
    ans += (end - start) 
    start, end = now_start, now_end

ans += (end - start)
print(ans)