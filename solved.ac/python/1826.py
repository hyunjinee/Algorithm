import heapq
n = int(input())
oil = []
for _ in range(n):
    oil.append(tuple(map(int, input().split())))
l, p = map(int, input().split())
oil.sort()
hq,i,cnt = [],0,0
while p < l:
    while i < n and oil[i][0] <= p:
        heapq.heappush(hq, -oil[i][1])
        i += 1
    if not hq:
        break
    p -= heapq.heappop(hq)
    cnt += 1
print(-1 if p < l else cnt)

# import sys, heapq
# input = sys.stdin.readline
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# l, p = map(int, input().split())
# a.sort(reverse=True)
# heap,count  = [],0
# while p < l:
#   while a and a[-1][0] <= p:
#     distance, fuel = a.pop()
#     heapq.heappush(heap, -fuel)
#   if not heap:
#     break
#   p -= heapq.heappop(heap)
#   count += 1
#   if l <= p:
#     print(count)
#     exit()
# print(-1)