import sys
import heapq
input = sys.stdin.readline
# 나돌아갈래~
n = int(input())
left , right = [ ] , []
for _ in range(n):
  num = int(input())
  if len(left) == len(right):
    heapq.heappush(left, (-num, num))
  else:
    heapq.heappush(right, (num, num))
  
  if right and left[0][1] > right[0][1]:
    left_value = heapq.heappop(left)[1]
    right_value= heapq.heappop(right)[1]
    heapq.heappush(right, (left_value, left_value))
    heapq.heappush(left, (-right_value, right_value))
  print(left[0][1])
# n = int(input())
# max_h, min_h = [],[]
# for i in range(n):
#   num =int(input())
#   if len(max_h) == len(min_h):
#     heapq.heappush(max_h, -num)
#   else:
#     heapq.heappush(min_h, num)
#   if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
#     max_value = heapq.heappop(max_h) * - 1
#     min_value = heapq.heappop(min_h)
#     heapq.heappush(max_h, min_value * -1)
#     heapq.heappush(min_h, max_value)

# print(max_h[0] * -1)
