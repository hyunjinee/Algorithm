#틱택토
import sys

# 3칸이 이어지는지 확인 (빙고인지 확인)
def checkBingo(xo):
    # 가로, 세로 체크
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==xo: return 1
        if board[0][i]==board[1][i]==board[2][i]==xo: return 1
    # 대각선 체크
    if board[0][0]==board[1][1]==board[2][2]==xo: return 1
    if board[0][2]==board[1][1]==board[2][0]==xo: return 1
    return 0

while True:
    temp = sys.stdin.readline().strip()
    if temp=='end': break

    result='invalid'
    xNum,oNum,board=0,0,[]
    for i in range(0,9,3):
        board.append(temp[i:i+3])
        for j in range(3):
            if board[i//3][j]=='X': xNum+=1
            elif board[i//3][j]=='O': oNum+=1

    if not xNum==oNum and not xNum==oNum+1:
        print(result)
        continue

    # 빙고인지 아닌지 확인
    xBingo = checkBingo('X')
    oBingo = checkBingo('O')

    if xNum==oNum and not xBingo and oBingo: result='valid'
    elif xNum==oNum+1:
        if xBingo and not oBingo: result='valid'
        elif not xBingo and not oBingo and xNum==5 and oNum==4: result='valid'
    print(result)

# import sys
# #sys.stdin = open("input.txt", 'r')
# input = sys.stdin.readline

# cases = [
#     [0,1,2], # 0
#     [3,4,5], # 1
#     [6,7,8], # 2
#     [0,3,6], # 3
#     [1,4,7], # 4
#     [2,5,8], # 5
#     [0,4,8], # 6
#     [2,4,6], # 7
# ]

# def check(board, pos):
#     base = board[pos[0]]
#     if all(map(lambda x:board[x] == base, pos)):
#         return base
    
# while True:
#     v = input().rstrip()
#     if v == 'end':
#         break
#     Xcnt, Ocnt = 0, 0
#     for c in v:
#         if c == 'X':
#             Xcnt += 1
#         elif c == 'O':
#             Ocnt += 1
#         else:
#             pass
    
#     x_bingo, o_bingo = 0, 0
#     for case in cases:
#         res = check(v, case)
#         if res == 'X':
#             x_bingo += 1
#         elif res == 'O':
#             o_bingo += 1
#         else:
#             pass
        
#     if Xcnt == Ocnt:
#         if o_bingo == 1 and x_bingo == 0:
#             print('valid')
#         else:
#             print('invalid')
#     elif Xcnt == 5 and Ocnt == 4:
#         if o_bingo == 0 and x_bingo >= 0:
#             print('valid')
#         else:
#             print('invalid')
#     elif Xcnt-1 == Ocnt:
#         if o_bingo == 0 and x_bingo > 0:
#             print('valid')
#         else:
#             print('invalid')
#     else:
#         print('invalid')

# # import sys
# # input = sys.stdin.readline



# # def check(x):
# #   print(x.find('.'))
  
# #   board = []
# #   temp = []
# #   for i in range(9):
# #     if i % 2 == 0 :
# #       pass



# # while True:
# #   ttt = input().rstrip()
# #   if ttt == 'end':
# #     break
# #   check(ttt)