import sys

input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0 
for i in range(1, w-1):
  left_max = max(heights[:i])
  right_max = max(heights[i+1:])

  compare = min(left_max, right_max)

  if heights[i] < compare:
    ans += compare - heights[i]
  
print(ans)