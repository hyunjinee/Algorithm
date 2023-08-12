n = int(input())
a = [list(map(str, input().split())) for _ in range(n)]
dic = {}

def add (dic, arr):
  if len(arr) == 0:
    return
  if arr[0] not in dic:
    dic[arr[0]] = {}
  # print(dic)
  # print(dic[arr[0]], "??")
  add (dic[arr[0]], arr[1: ])


def printTree (dic, leng ):
  for i in sorted(dic.keys()):
    print("--" * leng + i)
    printTree(dic[i], leng + 1)

for i in a:
  i = i[1:]
  add (dic, i)

printTree(dic, 0 )

# N = int(input())
# ant = {}

# for i in range(N):
#     name = list(input().split())
#     target_dict = ant
#     for j in name[1:]:
#         print(target_dict, "1")
#         if j not in target_dict:
#             target_dict[j] = {}
#         print(target_dict, "2")
#         target_dict = target_dict[j]
#         print(target_dict, "3")
# # print(target_dict)

# def getResult(t, i):
#     target_key = sorted(t.keys())
#     for s in target_key :
#         print('--'*i + s)
#         getResult(t[s],i+1)

# # getResult(ant,0)
# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # from collections import defaultdict
# # main = defaultdict(list)
# # robots = [ list(input().split()) for _ in range(n)]
# # for robot in robots:
# #   for i in range(int(robot[0])- 1):

# # import sys
# # n = int(sys.stdin.readline())
# # ant = []
# # for i in range(n):
# # 	ant.append(sys.stdin.readline().split()[1:])
# # print(ant)
# # tmp = []
# # for i in sorted(ant):
# # 	count = 0
# # 	for j in range(len(tmp)):
# # 		if tmp[j] == i[j]:
# # 			count += 1
# # 		else:
# # 			break
# # 	cnt = count
# # 	for j in range(count, len(i)):
# # 		print('--' * cnt + i[j])
# # 		cnt += 1
# # 	tmp = i

# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # ant = {}
# # for i in range(n):
# #   name = list(input().split())
# #   target_dict = ant
# #   for j in name[1:]:
# #     if j not in target_dict:
# #       target_dict[j] = {}
# #     print(target_dict, "before")
# #     print(target_dict[j] , "?")
# #     target_dict = target_dict[j]
# #     print(target_dict, "after")
# import sys
# input = sys.stdin.readline

# #   # if main[robot[1]] is None:
# #   #   main[robot[1]] = []
# # print(main)
# # print(robots)


# #
# #  import sys
# # input =sys.stdin.readline
# # from collections import defaultdict, deque
# # n = int(input())
# # main = defaultdict(list)
# # start = []
# # for _ in range(n):
# #   robot = list(input().split())
# #   print(robot)
# #   cnt = int(robot[0])
# #   path = robot[1:]
# #   start.append(robot[1])
# #   for i in range(cnt-1):
# #     main[path[i]].append(path[i+1])
# #   print(main)
# # start.sort() # sorting
# # for i in range(len(start)):
# #   print(start[i])
# #   visited = [start[i]]
# #   q = deque()
# #   q.append((start[i], start[i]))
# #   cnt = 0
# #   while q:
# #     cnt += 1
# #     now, toprint = q.popleft()
# #     print(toprint)
# #     for i in main[now]:
# #       if i not in visited:
# #         visited.append(i)
# #         q.append((i, '--' * cnt + i ))
# #         cnt += 1
    
#   # while True:
#   #   temp  = main[start[i]]
# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # ant = {}
# # for _ in range(n):
# #   name = list(input().split())
# #   target_dict = ant
# #   for i in name[1:]:
# #     if i not in target_dict:
# #       target_dict[i] =  {}
# #     target_dict = target_dict[i]
# #     print(target_dict)

# # import sys
# # input = sys.stdin.readline

# # N = int(input())
# # ant = {}

# # for i in range(N):
# #     name = list(input().split())
# #     target_dict = ant
# #     for j in name[1:]:
# #         if j not in target_dict:
# #             target_dict[j] = {}
# #         target_dict = target_dict[j]

# # def getResult(t, i):
# #     target_key = sorted(t.keys())
# #     for s in target_key :
# #         print('--'*i + s)
# #         getResult(t[s],i+1)

# # getResult(ant,0)

# # import sys
# # input =sys.stdin.readline
# # n  =int(input())
# # robots = []
# # for _ in range(n):
# #   robot = input().rstrip().split(" ")
# #   robots.append(robot)

# # print(robots)

