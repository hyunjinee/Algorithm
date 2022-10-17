import sys; input = sys.stdin.readline
from collections import deque

def move(rr, rc, br, bc, d):
  dist_r = dist_b = 0

  while True:
    nrr, nrc = rr + dr[d] , rc + dc[d]
    if arr[nrr][nrc] == '#':
      break
    if arr[nrr][nrc] == 'O':
      rr, rc = nrr, nrc
      break
    rr, rc = nrr, nrc

    dist_r += 1

  while True:
    nbr, nbc = br + dr[d], bc + dc[d]
    if arr[nbr][nbc] == '#':
      break
    if arr[nbr][nbc] == 'O':
      br, bc = nbr, nbc
      break
    br, bc = nbr, nbc
    dist_b += 1

  return (rr, rc, br, bc, dist_r, dist_b)


def bfs():
  while q: 
    rr, rc, br, bc, depth = q.popleft()
    for i in range(4):
      nrr, nrc, nbr, nbc, dist_r, dist_b = move(rr, rc, br ,bc, i)

      if arr[nrr][nrc] == 'O' and arr[nbr][nbc] == 'O':
        continue
      if arr[nbr][nbc] == 'O':
        continue
      if arr[nrr][nrc] == 'O':
        return depth + 1

      if nrr == nbr and nrc ==nbc:
        if dist_r > dist_b:
          nrr -= dr[i]
          nrc -= dc[i]
        else:
          nbr -= dr[i]
          nbc -= dc[i]

      if not visited[nrr][nrc][nbr][nbc]:
        visited[nrr][nrc][nbr][nbc] = True
        q.append((nrr, nrc, nbr, nbc, depth + 1))
  return - 1
      

if __name__ == '__main__':
  n, m = map(int, input().split())
  arr = [list(input().strip()) for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if arr[i][j] == 'R':
        rr, rc = i, j 
      elif arr[i][j] == 'B':
        br, bc = i, j

  
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]

  q = deque([(rr, rc, br, bc, 0)])

  visited = [[[[False] * m for _ in  range(n)] for _ in range(m)] for _ in range(n)]
  visited[rr][rc][br][bc] = True
  print(bfs())