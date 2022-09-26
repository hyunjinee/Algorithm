from collections import deque

def rotate_right(x, d):
  if x > 4 or gears[x-1][2] == gears[x][6]:
    return

  if gears[x-1][2] != gears[x][6]:
    rotate_right(x + 1, -d)
    gears[x].rotate(d)

def rotate_left(x, d):
  if x < 1 or gears[x][2] == gears[x+1][6]:
    return
  
  if gears[x][2] != gears[x+1][6]:
    rotate_left(x-1, -d)
    gears[x].rotate(d)



gears = {}

for i in range(1,5):
  gears[i] = deque((map(int, input())))

for _ in range(int(input())):
  x, d = map(int ,input().split())

  
  rotate_right(x + 1, -d)
  rotate_left(x - 1, -d)

  gears[x].rotate(d)

ans = 0
for i in range(4):
  ans += gears[i+1][0] * (2**i)
print(ans)