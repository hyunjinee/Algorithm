# # 아이스크림이 3개 생성된다.



# # 연결되어있는 부분은 아이스



# # 특정한 지점의 주변 상 하좌우 를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당지점을 방문한다.

# n, m = map(int, input().split())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y>=m:
#         return False

#         if graph[x][y] = 1:
#             graph[x][y] = 1
#             dfs(x -1, y)
#             dfs(x, y -1)
#             dfs(x+ 1, y)
#             dfs(x, y+1)
#         return True
#     return False



# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1


# print(result)