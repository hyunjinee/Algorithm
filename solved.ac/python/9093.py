import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  a=  input().rstrip()
  for b in a.split(" "):
    print(b[::-1], end=" ")
  print()
