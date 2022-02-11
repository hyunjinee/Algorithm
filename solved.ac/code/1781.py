import heapq
n = int(input())

array = []
for _ in range(n):
  deadline, cupNoodle = map(int, input().split())
  array.append((deadline, cupNoodle))

array.sort()
# print(array)
q = []

for i in array:
  heapq.heappush (q, i[1])
  # print(q)
  if i[0] < len(q):
    heapq.heappop(q)
  # print(q)
print(sum(q))


# import sys
# input = sys.stdin.readline

# n = int(input())
# worklist = []
# for _ in range(n):
#   worklist.append(list(map(int, input().split())))
# worklist.sort()
# # print(worklist)

# ans = 0
# for i, e in enumerate(worklist):
#   if i == len(worklist) -1 :
#     if e[0] != worklist[i - 1][0]:
#       ans += e[1]
    
#     break

#   if e[0] == worklist[i + 1][0]:
#     # print(e[0], worklist[i + 1][0])
#     continue
#   else: 

#     ans += e[1]

# print(ans)


  