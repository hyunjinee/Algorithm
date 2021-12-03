import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산


def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]

# 공기청정기 위쪽 이동


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)

# # 미세먼지는 확산된다.
# # (r,c )에 있는 미세먼지는 인접한 네 방향으로 확산
# # 양은 그 양의 /5 이고 소수점은 버림한다.
# # 남은 양은 Arc - 그양 * 방향의 개수

# # 공기 청정기 또한 작동한다.
# # 바람이 불면 미세먼지가 바람의 방향대로 순환한다.
# # 공기 청정기로 들어간 미세먼지는 정화된다.

# import sys

# input = sys.stdin.readline

# R, C, T = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(R)]

# # print(room)
# up = -1
# down = -1

# for i in range(R):
#     if room[i][0] == -1:
#         up = i
#         down = i + 1

#         break


# def diffusion():
#     dx = [-1, 0, 0, 1]
#     dy = [0, -1, 1, 0]

#     temp = [[0] * C for _ in range(R)]

#     for i in range(R):
#         for j in range(C):
#             if room[i][j] != 0 and room[i][j] != -1:
#                 tmp = 0
#                 for k in range(4):
#                     nx = dx[k] + i
#                     ny = dy[k] + j
#                     if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
#                         # temp[nx] += room[nx][ny] // 5
#                         tmp += room[i][j] // 5
#                 room[i][j] -= tmp
#     for i in range(R):
#         for j in range(C):
#             room[i][j] += temp[i][j]


# def air_up():
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = up, 1

#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == up and y == 0:
#             break

#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             direct += 1
#             continue
#         room[x][y], before = before, room[x][y]
#         x = nx
#         y = ny


# def air_down():
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = down, 1
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == down and y == 0:
#             break
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             direct += 1
#             continue
#         room[x][y], before = before, room[x][y]
#         x = nx
#         y = ny


# for _ in range(T):
#     diffusion()
#     air_up()
#     air_down()
# answer = 0
# for i in range(R):
#     for j in range(C):
#         if room[i][j] > 0:
#             answer += room[i][j]

# print(answer)

# # temp = [[0] * C for _ in range(R)]

# # d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# # def diffusion():
# #     for i in range(R):
# #         for j in range(C):
# #             if room[i][j] != -1:
# #                 for x, y in range(d):
# #                     if 0 <= i + x < R and 0 <= j + y < C and room[i + x][j + y] != -1:
# #                         temp[i + x][j + y] += room[i][j] / 5
# #                         room[i][j] -= room[i][j] / 5
# #     for i in range(R):
# #         for j in range(C):
# #             room[i][j] += temp[i][j]


# # def rotate():
# #     air = []
# #     for i in range(R):
# #         for j in range(C):
# #             if room[i][j] == -1:
# #                 air.append((i, j))
# #                 break
# #     up = air[0]
# #     down = air[1]
# #     # 어떻게 하면 순환을 잘 할 수 있을까?

# #     # up_list = []
# #     # for i in range(C):
# #     #     up_list.append(room[up[0]][i])
# #     # for i in range(up[0], -1, -1):
# #     #     up_list.append(room[i][-1])
# #     # for i in range(C, -1, -1):
# #     #     up_list.append(room[0][i])
# #     # for i in range(up[0]):
# #     #     up_list.append(room[i][0])

# # up_list.pop()
# # up_list.insert(0, 0)

# # room[up[0]] = up_list[0: 8]
# # for i in range(up[0], -1, -1):
# #     room[i][-1] = up_list[8 + (up[0] - i)]
# # for i in range(C, -1, -1):
# #     room[0][C] =


# # print(rotate())
