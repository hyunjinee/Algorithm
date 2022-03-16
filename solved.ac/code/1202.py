import sys,heapq
input =sys.stdin.readline
n, k = map(int,input().split())
diamonds = []
for _ in range(n):
  m, v = map(int, input().split()) # 무게 , 가격
  diamonds.append([m, v])
c = [int(input()) for _ in range(k)]
ans = 0
temp = []
diamonds.sort()
c.sort()
for cc in c:
  while diamonds and cc >= diamonds[0][0]:
    # print(diamonds)
    heapq.heappush(temp, -diamonds[0][1])
    heapq.heappop(diamonds)
  if temp:
    ans += heapq.heappop(temp)
  elif not diamonds:
    break
print(-ans)
# diamonds.sort(key=lambda x :  (x[0], -x[1]))
# c.sort()
# print(diamonds)
# print(c)

# ans = 0
# for i in range(len(c)):
#   # _sum = 0 
#   for j in range(0, len(diamonds)):
#     if diamonds[j][0] <= c[i] and diamonds[-1] != 'taken':
#       ans += diamonds[j][1]
#       diamonds.append('taken')
#       break






# # if n < k:
# #   _sum = 0 
# #   for _,b in diamonds:
# #     _sum += b
# #   print(_sum)
# #   exit()

