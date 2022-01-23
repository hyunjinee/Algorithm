import sys
input = sys.stdin.readline
s = set()
m = int(input())
for _ in range(m):
  o = input().rstrip()
  if o == 'all':
    s = set(range(1,21))
  elif o == 'empty':
    s = set()
  else: 
    a,b = o.split(" ")
    if a == 'add':
      s.add(int(b))
    elif a == 'check':
      if int(b) in s:
        print(1)
      else:
        print(0)
    elif a == 'toggle':
      if int(b) in s:
        s.remove(int(b))
      else:
        s.add(int(b))
    elif a == 'remove':
      if int(b) in s:
        s.remove(int(b))
