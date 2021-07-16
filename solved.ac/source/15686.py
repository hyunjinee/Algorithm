# #  도시의 칸은 빈칸 치킨집, 집중하나이다.


# # (r,c) 형태로 나타낸다.

# # r행 c열 

# # 치킨거리? ㅋㅋ 집과 가장 가까운 치킨 집 사이의 거리이다.
# # 즉 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨거리르 ㄹ가지낟.


# # 도시으 ㅣ치킨거리는 모든 집의 치킨거리의 합이다.

# # 이 도시에 있는 치킨집은 모두 프렌차이즈이고, 일부 치킨집을 패업시키려고한다.

# # 이 도시에서 가장 수익을 많이 낼수 있는 치킨집의 개수는 M개이다.

# # 도시에있는 치킨집중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야한다. 어떻게 고르면 도시의 치킨거리가 가장 작게 될지 구하는 프로그램

# # 첫 쭐 N, M

# import sys 
# input = sys.stdin.readline

# n, m = map(int, input().split())

# world = [list(map(int,input().split())) for _ in range(n)]

# chicken = []

# # 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 사실을 깨달음

# # 도시의 치킨거리가 가장.작게 되는 프로그램을 작성해라.
# # 모든 곳을  다 읽는데, 집은 무조건읽어 치킨거리의 최솟값을 구한데.
# # 치킨거리가 가장 작은 세곳을 고르는것 아닌가..>?
# def search(i, j):
#     distance = 0
#     dx = [0 , 0, 1, -1]
#     dy = [1, -1, 0 , 0]


#     while True:
#         distance += 1
        
#         for k in range(4):
#             if 0 <= i + dx[k] * distance <n and 0 <= j + dy[k] * distance < n:
                
#                 print(i + dx[k] , j + dy[k])
#                 # print(j + dy[k])
            

#                 if world[i + dx[k] * distance][j + dy[k] * distance] == 2:
#                     chicken.append(distance)
#                     return 


# # 폐업시키지 않을 치킨집 3개를 고른데.치킨거리가 멀면 폐업 시켜야겠네 치킨거리가 멀면 폐업이므로 치킨거리를 계산 sort하더라도 어떻게 찾음? 나모르게ㅜㅆ/ㅓ
# for i in range(n):
#     for j in range(n):
#         if world[i][j] == 1: 
            
#             search(i, j)

# print(chicken)
# chicken.sort()

# for i in range(m):
#     print(chicken[i])

# 치킨집위치를 저장
# 치킨집의 위치중  M개를 고른다.
# 치킨 거리를 계산하고 최솟값을 계산해서 업데이트를 계속한다.?


import itertools,sys, copy

n, m = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(n)]

chicken = []


for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i, j])
            arr[i][j] = 0

result = list(itertools.combinations(chicken, m))

min_distance = sys.maxsize
for i in range(len(result)):
    distance = 0 
    for j in range(n):
        for k in range(n):
            if arr[j][k]  == 1:
                temp = sys.maxsize
                for t in range(m):
                    temp = min(temp , abs(j - result[i][t][0] + abs(k - result[i][t][1])))
                distance += temp

    min_distance = min(min_distance, distance)

print(min_distance)