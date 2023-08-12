n, m, k = map(int, input().split())
A = [[5]*n for _ in range(n)]
addA = [list(map(int, input().split())) for _ in range(n)]
tree = [[{} for _ in range(n)] for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    x, y, a = map(int, input().split())
    tree[x-1][y-1][a] = 1
def spring():
  for i in range(n):
    for j in range(n):
      if tree[i][j]:
        tmp = {}
        die = 0
        for age in sorted(tree[i][j].keys()):
          if age * tree[i][j][age] <= A[i][j]:
            A[i][j] -= age * tree[i][j][age]
            tmp[age+1] = tree[i][j][age]
          else:
            survive = A[i][j] // age
            if not survive:
              die += (age // 2) * tree[i][j][age]
              continue
            A[i][j] -= age * survive
            tmp[age+1] = survive
            die += (age // 2) * (tree[i][j][age] - survive)
        tree[i][j] = tmp
        A[i][j] += die

def fall():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                num = 0
                for age in tree[i][j].keys():
                    if age % 5 == 0:
                        num += tree[i][j][age]
                if num:
                    for k in range(8):
                        ax = i + dx[k]
                        ay = j + dy[k]
                        if 0 <= ax < n and 0 <= ay < n:
                            if 1 not in tree[ax][ay].keys():
                                tree[ax][ay][1] = num
                            else:
                                tree[ax][ay][1] += num
def winter():
    for i in range(n):
        for j in range(n):
            A[i][j] += addA[i][j]
for _ in range(k):
    spring()
    fall()
    winter()
ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(tree[i][j].values())
print(ans)
# import sys
# input = sys.stdin.readline
# n,m,k=map(int,input().split())
# nour=[[5 for _ in range(n)] for _ in range(n)]
# nour_add = [list(map(int,input().split())) for _ in range(n)]
# tree = [[{} for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#   x,y,z = map(int,input().split())
#   tree[x-1][y-1][z] = tree[x-1][y-1].get(z, 0) + 1
# dr = [-1,-1,-1,0,0,1,1,1]
# dc = [-1,0,1,-1,1,-1,0,1]
# for _ in range(k):
#   # 봄이왔다.
#   for r in range(n):
#     for c in range(n):
#       if tree[r][c]:
#         die =0 
#         survived= 0 
#         temp = {}
#         for age in sorted(tree[r][c].keys()):
#           if nour[r][c] >= tree[r][c][age] * age:
#             nour[r][c] -= tree[r][c][age] * age
#             temp[age+1] = tree[r][c][age]
#           else:
#             survived = nour[r][c] // age
# import sys
# input = sys.stdin.readline

# N, M, K = map(int, input().rstrip().split(' '))
# nour = [[5 for _ in range(N)] for _ in range(N)]
# nour_add = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
# # 나무정보를 담고 있는 2차원 리스트 각 원소는 dictionary로 설정하여
# # 나이: 몇 그루
# # 위 정보를 담게 함
# tree = [[{} for _ in range(N)] for _ in range(N)]
# for _ in range(M):
#     x, y, z = map(int, input().rstrip().split(' '))
#     tree[x - 1][y - 1][z] = tree[x - 1][y - 1].get(z, 0) + 1

# dr = [-1, -1, -1, 0, 0, 1, 1, 1]
# dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# for _ in range(K):
#     # 봄: 나무가 자신의 나이만큼 양분을 먹는다.(어린 나이부터)
#     # 만약 양분이 부족하면 양분을 먹지 못하고 즉시 죽는다.
#     # 여름: 죽은 나무는 양분이 됨
#     for r in range(N):
#         for c in range(N):
#             if tree[r][c]:
#                 # 봄과 여름을 한 번에 계산
#                 # 주의할 점은 해당 구역에서 모든 나무들을 양분을 다 맥여놓고
#                 # 죽은나무가 양분이 되는 순서를 반드시 지켜야 함.
#                 die = 0
#                 survived = 0
#                 temp = {}
#                 for age in sorted(tree[r][c].keys()):
#                     if nour[r][c] >= tree[r][c][age] * age:
#                         nour[r][c] -= tree[r][c][age] * age
#                         temp[age + 1] = tree[r][c][age]
#                     else:
#                         # (양분 < 나무의 개수 * 나무의 나이) 경우에서
#                         # 양분 // 나이 
#                         # 이 계산을 하게 되면 살게되는 나무의 수가 구해짐
#                         survived = nour[r][c] // age
                        
#                         # 조건분기하는 이유는 temp[n] = 0이 되는 것이 없게 하기 위함
#                         # dictionary에서 key를 줄임으로써 반복 횟수를 줄이기 위함
#                         if survived == 0:
#                             die += (tree[r][c][age] - survived) * (age // 2)
#                             continue
#                         # 살아 남은 나무는 일단 먹기
#                         nour[r][c] -= survived * age
#                         # 잘 죽고
#                         die += (tree[r][c][age] - survived) * (age // 2)
#                         # 잘 살고
#                         temp[age + 1] = survived
#                 tree[r][c] = temp
#                 nour[r][c] += die

#     # 가을: 나무가 5살 단위로 번식. 인접 8칸에 나이가 1인 나무 생성
#     # 겨울: 양분 추가
#     for r in range(N):
#         for c in range(N):
#             if tree[r][c]:
#                 n = 0
#                 # 어차피 어린 나무가 생겨나는 개수는
#                 # 나이가 5로 나눠떨어지는 나무들의 개수만큼 8방향으로 생기게 됨
#                 for age in tree[r][c].keys():
#                     if age % 5 == 0:
#                         n += tree[r][c][age]
#                 # 무턱대고 반복시키는 것보다
#                 # 어린 나무가 생겨나는 조건이 되면(번식할 수 있는 나무가 있으면)
#                 # 그 때 번식시키기
#                 if n > 0: # 이게 포인트(시간 초과 해결의 중요한 코드)
#                     for i in range(8):
#                         nr, nc = r + dr[i], c + dc[i]
#                         if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
#                             tree[nr][nc][1] = tree[nr][nc].get(1, 0) + n
#             # 겨울
#             nour[r][c] += nour_add[r][c]

# print(sum([sum([sum(tree[r][c].values()) for c in range(N)]) for r in range(N)]))
# 엔곱하기 엔의 땅 구매
# 알 하고 씨로 나타냄
# r , c starts with 1
# make robot s2d2

# import sys,heapq
# from collections import deque
# input= sys.stdin.readline
# n, m, k = map(int, input().split())
# A = [list(map(int,input().split())) for _ in range(n)]
# board = [[5] * n for _ in range(n) ]
# q = []
# for _ in range(m):
#   x,y,z = map(int, input().split())
#   heapq.heappush (q, (z, x-1, y-1))
# alive = []
# dead = []
# dirs= [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
# while q and k > 0:
#   l = len(q)
#   for _ in range(l): # 봄
#     w, a, b =heapq.heappop(q)
#     if board[a][b] >= w:
#       board[a][b] -= w
#       w = w + 1 # 나이 증가
#       alive.append((w, a, b))
#     else:
#       # 나무죽음
#       dead.append((w//2, a, b))
    
#   for i in range(len(dead)): # 여름
#     ww,aa,bb = dead[i]
#     board[aa][bb] += ww
#   dead = [] # 죽은자들 초기화

#   for i in range(len(alive)): # 가을
#     www,aaa,bbb = alive[i]
#     if www % 5 == 0:
#       for d in dirs:
#         nx = aaa + d[0]
#         ny = bbb + d[1]
#         if 0 <= nx < n and 0 <= ny < n:
#           heapq.heappush(q, (1, nx, ny))
#           alive.append((1, nx, ny))


#   for i in range(n):
#     for j in range(n):
#       board[i][j] += A[i][j]
    
#   k -= 1

# print(alive)

# dead = []
# while q:
#   l = len(q)
#   for _ in range(l):
#     a,b,c = heapq.heappop(q)
#     if board[b][c] > a:
#       board[b][c] - a
#       a = a + 1 # 나이 1증가
#       # heapq.heappush(q, (a, b, c))
#     else:
#       # 나무가 죽는다.
#       w = a // 2
#       dead.append((w,b,c)) # 좌표 저장후 반만큼 영양분 dead에 저장
#       continue
#   for  i in range(len(dead)):
#     ww,bb,cc = dead[i]
#     board[bb][cc] += ww
#   #  여름
  
