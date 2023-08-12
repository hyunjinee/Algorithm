import sys, heapq; input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  lst = list(map(int, input().split()))
  ans = 0

  q = []

  for i in lst:
    heapq.heappush(q, i)

  while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    ans += a + b

    heapq.heappush(q, a + b)
  
  print(ans)