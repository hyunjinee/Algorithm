import sys
input = sys.stdin.readline


n,m = map(int, input().split())

l = list(map(int,input().split()))

l.sort()

s = []

def dfs():

  if len(s) == m:
    print(' '.join(map(str,s)))
    return 

  for i in range(n):
    if len(s) > 0 and l[i] >= s[-1]:
      s.append(l[i])
      dfs()
      s.pop()
    if len(s) == 0:
      s.append(l[i])
      dfs()
      s.pop()
dfs()