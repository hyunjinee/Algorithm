import sys
input = sys.stdin.readline
n = int(input())

import heapq

cards = list(int(input()) for _ in range(n))
heapq.heapify(cards)
result = 0

while len(cards) != 1: 
  num1 = heapq.heappop(cards)
  num2 = heapq.heappop(cards)
  _sum = num1 + num2
  result += _sum

  heapq.heappush(cards, _sum)

print(result)