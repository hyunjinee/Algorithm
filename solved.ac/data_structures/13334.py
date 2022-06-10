import sys,heapq
input = sys.stdin.readline
n = int(input())
gugan = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())

gugan.sort(key= lambda x: x[1])
# print(gugan)

ans = -1 
heap =[]
for s,e in gugan:
  lim = e - d
  if s >= lim:
    heapq.heappush(heap, s)
  while heap and heap[0] < lim:
    heapq.heappop(heap)
  ans = max(ans, len(heap))
print(ans)
