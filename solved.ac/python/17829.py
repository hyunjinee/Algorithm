import sys
input =sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
def polling(board,n):
  if n == 1:
    return board[0][0]
  new_board = [[] for _ in range(n//2)]
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      new_board[i//2].append(sorted([board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]])[2])
  return polling(new_board, n//2)
print(polling(board, n))