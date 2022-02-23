import sys
import heapq
input = sys.stdin.readline
n, m = map(int,input().split())
heap = []

for _ in range(n):

  heap.append(int(input()))

heapq.heapify(heap)
print(heap)
for _ in range(m):
  a, b = map(int, input().split())


