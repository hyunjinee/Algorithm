import sys
input = sys.stdin.readline

for _ in range(int(input())):
  r,c = map(int, input().split())
  board = [list(map(int, input().rstrip())) for _ in range(r)]
  direction = [list(map(int, input().rstrip().split(" "))) for _ in range(r)]

  print(board)
  print(direction)