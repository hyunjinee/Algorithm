from collections import deque


def bfs():
  q = deque()
  q.append((A,B))
  check[A][B] = True
  while q:
    x, y = q.popleft()
    z = D - x -y
    if x == y == z:
      print(1)
      return 
    for a,b  in (x,y), (x, z), (y, z):
      if a < b:
        b -= a
        a += a
      elif a>b:
        a -= b
        b += b
      else:
        continue
      c = D - a - b
      X = min (a, b, c)
      Y = max (a, b, c)
      if not check[X][Y]:
        q.append((X,Y))
        check[X][Y] = True
  print(0)

def solve():
  if D % 3:
    print(0)
    return
  else:
    bfs()

A, B, C = map(int, input().split())
D = A + B + C
check = [[False] * D for _ in range(D)]

solve()

# a,b,c = map(int,input().split())

# from collections import deque

# _sum = a + b + c


# def bfs(x, y , z):
#   q = deque()
#   if x != y:
#     if x < y:
#       q.append((x + x, y - x))
#   if x != z:
#     if x < z:
#       q.append((x + x,z - x))
#   if y != z:
#     if y < z:
#       q.append((y + y,z - y))

#   while q:
#     aa, bb, cc = q.popleft()

  
