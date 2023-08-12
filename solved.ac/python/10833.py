import sys
input = sys.stdin.readline
n = int(input())
_sum = 0
for _ in range(n):
  a, b = map(int,input().split())
  _sum += b%a
print(_sum)