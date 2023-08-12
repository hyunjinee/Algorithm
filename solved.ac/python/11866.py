from collections import deque
queue = deque()
answer = []
n, k = map(int ,input().split())

for i in range(1, n+1):
  queue.append(i)
while queue:
  for i in range(k-1):
    queue.append(queue.popleft())
  answer.append(queue.popleft())
print("<", end='')
for i in range(len(answer) - 1):
  print(answer[i], end=', ')
print(answer[-1], end=">")
# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# lst = [i for i in range(0, n+1)]
# start = 0
# visited = [False] * (n + 1)
# visited[start] = True

# while sum(visited) != n:
#   print(visited)

#   temp  = 0

#   while temp <= k:
#     index = start + temp
#     index = index % n

#     if temp == k:
#       if not visited[index]:
#         visited[index] = True
#       break
  
#     if not visited[index]:
#       temp += 1
#     if visited[index]:
#       continue
#   start = start + k
#   start = start % n
  

# # while sum(visited) != n:
# #   print(visited)
# #   temp  = 0 
# #   for i in range(1, k + 1):
# #     if i == k and temp == k:
# #       start = (start + 1) % n
# #       visited[start] = True
# #       print(lst[start])
# #     elif i == k and temp != k:
# #       break
  

# #     if start + i > n:
# #       start = (start + i) % n
# #       if visited[start] == False:
# #         temp += 1
# #         if i == k:

# #           visited[start] = True
        

# #     if start + i <= n and not visited[start + i]:
# #       temp += 1
# #       if i == k :
# #         start = (start + i) % n
# #         visited[start] = True
    

   
      



# #   if start > n:
# #     start %= n
  
