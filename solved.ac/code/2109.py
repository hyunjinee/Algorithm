import sys
import heapq


input = sys.stdin.readline

n = int(input())
if n == 0: 
  print(0)
  exit()

data = []
for _ in range(n):
  amount, deadline = map(int,input().split())
  data.append((deadline, amount))

data.sort()

q =  []

for deadline, amount in data:
  heapq.heappush(q, amount)
  if len(q) > deadline: 
    heapq.heappop(q)

print(sum(q))

# import sys
# input = sys.stdin.readline
# # d일 안에 와서 강연을 해주면 p만큼의 강연료를 지불한다. 근데 이를 바탕으로 가장 돈을 많이 벌수 있도록 순회강연을 
# # 한다. 강연의 특성상 이 학자는 하루에 최대 한곳에서만 강연을 할수 있.


# n = int(input())
# suggested = [list(map(int, input().split())) for _ in range(n)]
# # p ,d 

# # 위상 정렬 느낌으로 가도 될것 같은데
# # d -> indegree

# suggested.sort(key=lambda x: (x[1], -x[0]))

# # print(suggested)
# before = -1
# sum = 0 
# for i in range(len(suggested)):
#   if suggested[i][1] > before:
#     sum += suggested[i][0]
#   before = suggested[i][1]
# print(sum)
