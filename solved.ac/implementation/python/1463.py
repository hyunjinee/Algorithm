import sys
from collections import deque

input = sys.stdin.readline

x = int(input())

q = deque([(x,0)])

visited =[False] * (x + 1)
visited [x] = True

while q:
  number, count = q.popleft()

  if number == 1:
    print(count)
    break
  if number % 3 == 0 and not visited[number // 3]:
    visited[number // 3] = True
    q.append((number//3, count+1))
  if number % 2 == 0 and not visited[number // 2]:
    visited[number // 2] = True
    q.append((number//2, count+1))
  
  q.append((number-1, count+1))


