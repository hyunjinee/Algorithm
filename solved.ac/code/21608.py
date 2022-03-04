import sys, heapq
input = sys.stdin.readline
n = int(input())
school = [[0] * n for _ in range(n)]
like = {}
for t in range(n**2):
  temp = list(map(int,input().split()))
  a, b = temp[0], temp[1:]
  like[a] = b
  if t == 0:
    school[1][1] = a
    continue
  q = [ ]
  for i in range(n):
    for j in range(n):
      if school[i][j] == 0:
        like_cnt ,empty_cnt = 0, 0
        for dx, dy in (1,0), (-1, 0) ,(0,1), (0, -1):
          if 0 <= i + dx < n and 0 <= j + dy < n:
            if school[i + dx][j + dy] == 0:
              empty_cnt += 1
            elif school[i + dx][j + dy] in like[a]:
              like_cnt += 1
        heapq.heappush (q, (-like_cnt, -empty_cnt, i, j))
  best = heapq.heappop(q)
  school[best[2]][best[3]] = a

def calculate() :
  score = [0, 1, 10 ,100, 1000]
  res = 0 
  for i in range(n):
    for j in range(n):
      cnt = 0
      me = school[i][j]
      for dx, dy in (1,0), (-1, 0) ,(0,1), (0, -1):
        if 0 <= i + dx < n and 0 <= j + dy < n:
          if school[i + dx][j + dy] in like[me]:
            cnt += 1
      res += score[cnt]
  return res
print(calculate())




#                     cnt += 1
#             res += score[cnt]
#     return res




# import sys
# from collections import defaultdict
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# input = sys.stdin.readline

# n = int(input())
# school = [[ 0] * n  for _ in range(n) ]
# love = defaultdict(list)
# result = 0
# for _ in range(n * n):
#   temp = list(map(int, input().split()))
#   love[temp[0]] = temp[1:]
#   max_x = 0 
#   max_y = 0
#   max_like = -1
#   max_empty = -1

#   for i in range(n):
#     for j in range(n):
#       if school[i][j] == 0:
#         likecnt = 0
#         emptycnt = 0
#         for k in range(4):
#           nx = i + dx[k]
#           ny = j + dy[k]
#           if 0 <= nx < n and 0 <= ny < n:
#             if school[nx][ny] in temp:



# student = [list(map(int,input().split())) for _ in range(n * n)]
# for stu in student:

  


