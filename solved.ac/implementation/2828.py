import sys; input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

start = 1
end = m
distance = 0

for _ in range(j):
  p = int(input())

  if p < start:
    distance += (start - p)
    start = p
    end = p + m - 1

  elif p > end: 
    distance += (p - end)
    end = p

    start = end - m + 1
print(distance)
