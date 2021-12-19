import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  l, n = map(int, input().split())
  ants = []
  for i in range(n) :
    ants.append(int(input()))
  minant = 0
  maxant = 0
  for ant in ants:
    if ant > l - ant :
      if minant < l -ant:
        minant = l -ant
      if maxant < ant:
        maxant = ant
    else:
      if minant < ant:
        minant = ant
      if maxant < l -ant:
        maxant = l -ant
  # print(minant, maxant)
  print(minant,maxant)
