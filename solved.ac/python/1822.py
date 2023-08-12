import sys
input = sys.stdin.readline

aCount,bCount = map(int,input().split())
aList = list(map(int,input().split()))
bList = list(map(int,input().split()))

c = set(aList) - set(bList)

if len(c) == 0:
  print(0)
  exit()
print(len(list(c)))
print(*sorted(list(c)))