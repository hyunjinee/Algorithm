import sys

input = sys.stdin.readline
n, h = map(int, input().rstrip().split())
up = [0] * (h + 1)
down = [0] * (h + 1)
answer = []

for i in range(1, n + 1):
    size = int(input())
    if i % 2 == 1:  # 석순(아래)
        down[size] += 1
    else:  # 종유석 (위)
        up[size] += 1

for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

# 파괴되는 종유석, 석순 검사
for section in range(1, h + 1):
    # 1 ~ h번째 구간까지 존재.
    # 구간당 개똥벌레가 -0.5에 있다고 인식
    answer.append(down[section] + up[h + 1 - section])

tot = 0
m = min(answer)
for i in answer:
    if i == m:
        tot += 1
print("{0} {1}".format(m, tot))

# import sys
# input=sys.stdin.readline

# n, h = map(int, input().split())
# a=[int(input()) for _ in range(n)]

# jong=[0]*(h+1)
# suck=[0]*(h+1)

# for i in range(n):
#     if i%2!=0:
#         jong[h-a[i]+1]+=1
#     else:
#         suck[a[i]]+=1

# for i in range(len(suck)-1, 0, -1):
#     suck[i-1]+=suck[i]

# for j in range(1, len(jong)):
#     jong[j]+=jong[j-1]

# res=[]
# for k in range(1, len(jong)):
#     res.append(jong[k]+suck[k])

# print(min(res), res.count(min(res)))

# # import sys

# # input = sys.stdin.readline
# # n, h = map(int, input().rstrip().split())
# # up = [0] * (h + 1)
# # down = [0] * (h + 1)
# # answer = []

# # for i in range(1, n + 1):
# #     size = int(input())
# #     if i % 2 == 1:  # 석순(아래)
# #         down[size] += 1
# #     else:  # 종유석 (위)
# #         up[size] += 1

# # for i in range(h - 1, 0, -1):
# #     up[i] += up[i + 1]
# #     down[i] += down[i + 1]

# # # 파괴되는 종유석, 석순 검사
# # for section in range(1, h + 1):
# #     # 1 ~ h번째 구간까지 존재.
# #     # 구간당 개똥벌레가 -0.5에 있다고 인식
# #     answer.append(down[section] + up[h + 1 - section])

# # tot = 0
# # m = min(answer)
# # for i in answer:
# #     if i == m:
# #         tot += 1
# # print("{0} {1}".format(m, tot))


# # # import sys
# # # input = sys.stdin.readline
# # # n, h = map(int, input().split())
# # # board = [[0] * n for _ in range(h)]

# # # for i in range(n):
# # #   obstacle = int(input())
# # #   for j in range(obstacle):
# # #     if i % 2 == 0 :
# # #       board[h  - (j + 1)][i] += 1
# # #     else:
# # #       board[j][i] += 1

# # # # 장애물의 최솟값 그리고 그 수
# # # min_obstacle = sys.maxsize
# # # cnt = 0 
# # # for a in board:
# # #   if sum(a) < min_obstacle:
# # #     min_obstacle = sum(a)
# # #     cnt = 0 
# # #     cnt += 1
# # #   elif sum(a) == min_obstacle:
# # #     cnt += 1
# # #   else:
# # #     continue

# # # print(min_obstacle, cnt)




  
