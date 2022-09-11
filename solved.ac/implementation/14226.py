from collections import deque
n = int(input())
dist = [[-1]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer)

# from collections import deque

# n = int(input())

# clipboard = 0
# q = deque([[1, 0]])
# vis = [[0] * 1001 for i in range(1001)]
# vis[1][0] = 1

# if n == 1:
#     print(0)
#     exit()

# count = -1
# while q:
#     count += 1
#     # bfs 수행
#     for _ in range(len(q)):
#         emoticon, clipboard = q.popleft()
#         if emoticon == n:
#             print(count)
#             exit()
#         # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
#         # 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다.
#         if not vis[emoticon][emoticon]:
#             q.append([emoticon, emoticon])
#             vis[emoticon][emoticon] = 1
#         # 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
#         if 1 <= emoticon + clipboard <= n and not vis[emoticon + clipboard][clipboard]:
#             q.append([emoticon + clipboard, clipboard])
#             vis[emoticon + clipboard][clipboard] = 1
#         # 화면에 있는 이모티콘 중 하나를 삭제한다.
#         if emoticon - 1 >= 0 and not vis[emoticon - 1][clipboard]:
#             q.append([emoticon - 1, clipboard])
#             vis[emoticon - 1][clipboard] = 1

# # from collections import deque
# # n = int(input())

# # dp = [[float('inf')] * (n + 2) for _ in range(1001)]
# # q = deque([(1, 0, 0)])

# # while q:
# #   num,t,clip = q.popleft()
# #   if num == n:
# #     print(t)
# #     break


# #   t += 1

# #   for dnum in num+clip, num - 1:

# # # from collections import deque

# # # s = int(input())
# # # dist = [[-1] * (s+1) for _ in range(s+1)]
# # # q= deque()

# # # q.append((1, 0)) # 화면 이모티콘 개, 클립보드 이모티콘 개수
# # # dist[1][0] = 0

# # # while q:
# # #   s, c = q.popleft()
# # #   if dist[s][s] == -1 :
# # #     dist[s][s] = dist[s][c] + 1
# # #     q.append((s, s))
# # #   if s 


# # # # from collections import deque

# # # # s = int(input())
# # # # def bfs(): 

# # # #   q = deque()
# # # #   q.append([1, 0, 0]) # count, clipboard, time

# # # #   while q:
# # # #     count, clipboard, time = q.popleft()

# # # #     if count == s:
# # # #       return time


# # # #     if count < s:
# # # #       q.append([count + clipboard, clipboard, time + 1])
# # # #       q.append([count - 1, clipboard, time + 1])
# # # #       q.append([count, count, time + 1])

# # # # print(bfs())