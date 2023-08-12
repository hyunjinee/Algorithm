import sys
import heapq

input = sys.stdin.readline


t = int(input())

for _ in range(t):

  heap=  []
  k = int(input()) #  연산의 개수

  for i in range(k):
    a, b = input().rstrip().split()
    if a == 'I':
      heapq.heappush(heap, b)
    elif a == 'D':
      if len(heap) == 0:
        continue
      else:
        if b == '1':

          heap =  heap[:-1]
        else:
          heapq.heappop(heap)
  
  if len(heap) == 0:
    print("EMPTY")
  else: print(heap[0], heap[-1])