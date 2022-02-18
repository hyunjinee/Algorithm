from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
s = [list(input().strip()) for i in range(12)]
result = 0
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if s[j][i] != "." and s[k][i] == ".":
                    s[k][i] = s[j][i]
                    s[j][i] = "."
                    break

def bfs(i, j, char):
    q = deque()
    q.append([i, j])
    chain.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and s[nx][ny] == char:
                visit[nx][ny] = 1
                q.append([nx, ny])
                chain.append([nx, ny])

while True:
    isTrue = False
    visit = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if s[i][j] != "." and visit[i][j] == 0:
                visit[i][j] = 1
                chain = []
                bfs(i, j, s[i][j])
                if len(chain) > 3:
                    isTrue = True
                    for x, y in chain: s[x][y] = "."
    if not isTrue: break
    down()
    result += 1
print(result)

# # 필드에 여러가지 색깔으 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올때까지
# # 아래로 떨어진다. 



# # 뿌요를 놓고 난후 같은색 뿌요가 4개 이상 상하좌우로 연결되엉ㅆ으면 같은 색뿌요들이 한꺼번에 사라짐 
# # 이때 1연쇄가 시작된다.

# ## 뿌요들이 없어지고 나서 위에 다른뿌요들이 있다면, 역시 중력의영향을 받아서 차례대로 떨어짐
# # 연쇄 추가


# # 남규는 최근 뿌요뿌요 게임에 빠졌다. 이 게임은 1:1 로 붙는 대전게임이라 잘쌓는것도 중요하지만 상대방이
# # 터뜨린다면 연쇄가 몇번이 될지 바로 파악할 수 있는 능력도 필요
# # 상대방의 필드가 주어졌을때 연쇄가 몇번 연속으로 일어날지 남규를 도와주자.


# import sys
# from collections import deque
# input = sys.stdin.readline
# # 12 line 6 개의 문자
# # . empty space  and other is puyo
# # R ,G ,B  ,P, Y
# # 연쇄가 0이면 0출력 몇연쇄가 가능한지 출력

# puyo = [list(input().rstrip()) for _ in range(12)]
# # print(puyo)

# def bfs(y,x):
#   visited = [[False]*6 for _ in range(12)]
#   q = deque()
#   q.append((y,x))
#   visited[y][x] = True
#   cnt = 0 
#   deleted_index = []
#   deleted_index.append((y,x))
#   while q:
#     y,x = q.popleft()
#     cnt += 1
#     for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
#       ny, nx = y+dy, x+dx
#       if 0<=ny<12 and 0<=nx<6 and not visited[ny][nx] and puyo[ny][nx] == puyo[y][x]:
#         q.append((ny,nx))
#         visited[ny][nx] = True
#         deleted_index.append((ny,nx))
  
#   if cnt >= 4:
#     return deleted_index
#   else:
#     return []

# main_delete = [0]
# ans = 0

# def chain() :
#   global main_delete
#   global ans
#   for i in range(12):
#     for j in range(6):
#       if puyo[i][j] == '.':
#         continue
#       else:
#         main_delete += bfs(i,j)

#   if len(main_delete) > 1:
#     ans += 1
#   else:
#     return

#   for y, x in main_delete:
#     puyo[y][x] = '.'

# def down_puyo():
#   global puyo
#   for i in range(11, 0, -1):
#     for j in range(6):
#       for k in range(i-1, 0, -1):
#         if puyo[i][j] == '.' and puyo[k-1][j] != '.':
#           puyo[i][j] = puyo[k-1][j]
#           puyo[k-1][j] = '.'
#         else:
#           continue


      
#   # for i in range(12):
#   #   for j in range(6):
#   #     if puyo[i][j] == '.':
#   #       continue
#   #     else:
#   #       for k in range(i+1,12):
#   #         if puyo[k][j] == '.':
#   #           puyo[k][j] = puyo[k-1][j]
#   #           puyo[k-1][j] = '.'
#   #         else:
#   #           break

# def check ():
#   for i in range(12):
#     for j in range(6):
#       if puyo[i][j] == '.':
#         continue
#       else: return True 

#   return False


# while check() and len(main_delete) != 0 :
#   main_delete = []
#   chain()
#   down_puyo()

# print(ans)

# # chain()
# # for pu in puyo:
# #   print(pu)
# # down_puyo()
# # for pu in puyo:
# #   print(pu)