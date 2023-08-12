import sys
input = sys.stdin.readline
for _ in range(int(input())):  
  n,m =map(int,input().split())
  books = [False] * (n+1)
  r = [list(map(int,input().split())) for _ in range(m)]
  r.sort(key = lambda x : x[1])
  cnt = 0 
  while r: 
    a, b = r.pop(0)
    for i in range(a, b+1):
      if not books[i]:
        cnt += 1
        books[i] = True
        break
  print(cnt)