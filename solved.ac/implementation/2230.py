import sys; input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

start = 0 
end = 0
min_value = sys.maxsize

while start < n and end < n:
  result =  a[end] - a[start]

  if result >= m: 
    min_value = min(result, min_value)
    start += 1

  else:
    end += 1

print(min_value)