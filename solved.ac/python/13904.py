import sys,heapq
read = sys.stdin.readline
N = int(read())
arr = []
for _ in range(N):
    d,n = map(int,read().split())
    arr.append([d,n])
arr.sort()
heap = []
for i in arr:
    heapq.heappush(heap,i[1])
    if len(heap) > i[0]:
        heapq.heappop(heap)
print(sum(heap))

# import sys
# input = sys.stdin.readline
# n = int(input())
# homeworks = [list(map(int, input().split())) for _ in range(n)]
# homeworks.sort()
# # print(homeworks)
# can = []
# date = homeworks[-1][0]
# answer = 0
# while True:
#   if date == 0:
#     break
#   while homeworks and  homeworks[-1][0] >= date:
#     can.append(homeworks.pop()[1])
#   date -= 1
#   if not can:
#     continue
#   can.sort()
#   answer += can.pop()
# print(answer)
