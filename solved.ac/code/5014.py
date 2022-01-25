from collections import deque
import sys
input = sys.stdin.readline
def bfs(i):
    q = deque()
    q.append(i)
    visit = [0 for i in range(f)]
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dire[i]
            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                s_[nx] = s_[x] + 1
                visit[nx] = 1
f, s, g, u, d = map(int, input().split())
s_ = [-1 for i in range(f)]
dire = [u, -d]
s_[s - 1] = 0
bfs(s - 1)
print(s_[g - 1] if s_[g - 1] != -1 else "use the stairs")

# f,s,g,u,d = map(int,input().split())
# # f: building height
# # s: start point
# # g: goal point
# # u: up
# # d: down
# import sys
# INF = sys.maxsize
# visited = [False for _ in range(f+1)]
# building = [INF for _ in range(f+1)]

# visited[s] = True


# from collections import deque
# def bfs (start,cnt):
#   q = deque()
#   q.append((start, cnt))

#   while q:
#     now, w = q.popleft()
#     visited[now] = True
#     if building[now] >= w:
#       building[now] = w
#     if now + u <= f and not visited[now+u]:
#       q.append((now+u, w+1))
#     if now - d >= 1 and not visited[now-d]:
#       q.append((now-d, w+1))
  

# bfs(s, 0)
# if building[g] == INF:
#   print("use the stairs")
# else:
#   print(building[g])