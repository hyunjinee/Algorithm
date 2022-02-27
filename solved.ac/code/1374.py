import sys
import heapq

N = int(sys.stdin.readline())
lesson = []
for _ in range(N):
    _, b, c = map(int, sys.stdin.readline().split())
    lesson.append((b, c))

lesson.sort(key=lambda x: (x[0], x[1]))

queue = []
for s, e in lesson:
    if queue and queue[0] <= s:
        heapq.heappop(queue)

    heapq.heappush(queue, e)
    print(queue)

print(len(queue))

# import sys, heapq
# input =sys.stdin.readline
# n = int(input())
# std =[ ]
# for _ in range(n):
#   i, s, e = map(int, input().split())
#   std.append([s, e])
# std.sort(key = lambda x : x[0])
# check, res = [], 0
# for val in std:
#   if check and check[0] <= val[0]:
#     heapq.heappop(check)
#   heapq.heappush(check, val[1])

#   if res < len(check):
#     res = len(check)
# print(res)

# # import heapq
# # import sys

# # n = int(sys.stdin.readline())

# # heap = []
# # q = []
# # count = 0
# # for _ in range(n):
# #     num, start, end = map(int,sys.stdin.readline().split())
# #     heapq.heappush(heap, [start,end,num])

# # start, end, num = heapq.heappop(heap)
# # heapq.heappush(q, end)
# # while heap:
# #     start, end, num = heapq.heappop(heap)
# #     if q[0] <= start:
# #         heapq.heappop(q)
# #     heapq.heappush(q, end)

# # print(len(q))

# # # import sys
# # # from collections import deque
# # # input =sys.stdin.readline
# # # n = int(input())
# # # ans = -1

# # # startTime = []
# # # endTime = []
# # # temp =[]
# # # for i in range(n):
# # #   a, b, c = map(int, input().split())
# # #   startTime.append([b, a])
# # #   endTime.append([c, a])

# # # startTime.sort(reverse=True)
# # # endTime.sort(reverse=True)

# # # for time in range(endTime[0][0] + 1) :
# # #   while startTime and time >= startTime[-1][0]:
# # #     t, idx = startTime.pop()
# # #     temp.append(idx)

# # #   while endTime and time >= endTime[-1][0]:
# # #     t, idx = endTime.pop()
# # #     temp.remove(idx)
  
# # #   if len(temp) > ans:
# # #     ans = len(temp)
  
# # # print(ans)

# # # # time = [0] * (100000000)
# # # # for _ in range(n):
# # # #   a, b, c = map(int,input().split())
# # # #   for i in range(b, c+1):
# # # #     time[i] += 1

# # # # print(time)
