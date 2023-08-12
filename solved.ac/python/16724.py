import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = [input().rstrip() for _ in range(n)]
direction = dict() 
direction['D']=[0,1] 
direction['L']=[-1,0] 
direction['R']=[1,0] 
direction['U']=[0,-1]
parent = [i for i in range(n * m)]

def find (x):
  if x == parent[x] : return x
  parent[x] = find(parent[x])
  return parent[x]
def union(x,y):
  x = find(x)
  y = find(y)
  if x == y : return 
  if x < y: parent[y] = x
  else: parent[x] = y

for num in range(n*m):
  x = num % m
  y = num // m

  cur = board[y][x]
  nx = x + direction[cur][0]
  ny = y + direction[cur][1]

  next_num = ny * m + nx
  if next_num < 0 or next_num >= n * m : continue
  union(num, next_num)
answer = 0
visited = dict()
for i in range(n*m):
  if find(parent[i]) not in visited: 
    answer += 1
    visited[parent[i]] = True
print(answer)
