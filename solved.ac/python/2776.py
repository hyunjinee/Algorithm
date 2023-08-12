import sys;input=sys.stdin.readline
for _ in range(int(input())):
  n= int(input())
  first = set(map(int,input().split()))
  m = int(input())
  second = list(map(int,input().split()))

  for se in second:
    if se in first:
      print(1)
    else: print(0)