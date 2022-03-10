import sys
from collections import deque
input = sys.stdin.readline
def bfs():
  q = deque()
  q.append((home[0], home[1]))
  while q:
    y, x = q.popleft()
    if abs(y - fest[0]) + abs(x - fest[1]) <= 1000:
      print("happy")
      return 
    for i in range(n):
      if not visited[i]:
        new_y, new_x = conv[i]
        if abs(y - new_y) + abs(x - new_x) <= 1000:
          q.append((new_y, new_x))
          visited[i] = 1
  print("sad")
  return

for _ in range(int(input())):
  n = int(input())
  home = list(map(int, input().split()))
  conv = []
  for i in range(n):
    y, x = map(int, input().split())
    conv.append((y, x))
  fest = list(map(int, input().split()))
  visited = [0 for i in range(n+1)]
  bfs()
#   n  = int(input())
#   mid = []
#   for i in range(n + 2) :
#     if i == 0:
#       start = list(map(int, input().split()))
#     elif i == n + 1:
#       end =  list(map(int, input().split()))
#     else:
#       mid.append(list(map(int, input().split())) )
  
#   print(start, mid, end)