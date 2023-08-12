import sys; input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
c = int (input())

arr = sorted([int(input()) for _ in range(n)], key=lambda x:-x)

for x in arr:
  if a * x < b * c:
    break
  a += b
  c += x

print(int(c/a))