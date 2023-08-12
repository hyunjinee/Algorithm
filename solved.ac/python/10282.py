import sys
import heapq

INF = int(1e9)
input = lambda: sys.stdin.readline().strip()

def solution():
  n, d, c = map(int, input().split())
  network = [[] for _ in range(n + 1)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    network[b].append((a, s))
  
  cnt, time = 0, -1
  visited = [INF] * (n + 1)
  visited[c] = 0
  hq = [(0, c)]
  while hq:
    ctime, cur = heapq.heappop(hq)
    if visited[cur] < ctime:
      continue

    time = max(time, ctime)
    cnt += 1
    
    for cp, t in network[cur]:
      ntime = ctime + t
      if visited[cp] > ntime:
        visited[cp] = ntime
        heapq.heappush(hq, (ntime, cp))

  print(cnt, time)
        
if __name__ == '__main__':
  for _ in range(int(input())):
    solution()

# import sys,heapq
# input = sys.stdin.readline
# INF = sys.maxsize

# def dijkstra(start):
#   q = []
#   heapq.heappush(q, [0, start])
#   dist = [INF for _ in range(n+1)]
#   dist[start] = 0 
#   while q:
#     we, nu = heapq.heappop(q)
#     for ne, nw in s[]

# t = int(input())
# for _ in range(t):
#     n, d, start = map(int, input().split())
#     s = [[] for i in range(n + 1)]
#     for i in range(d):
#         a, b, c = map(int, input().split())
#         s[b].append([a, c])
#     dp = dijkstra(start)
#     max_dp = 0
#     cnt = 0
#     for i in dp:
#         if i != inf:
#             if max_dp < i:
#                 max_dp = i
#             cnt += 1
#     print(cnt, max_dp)


# # from collections import deque
# # input =sys.stdin.readline

# # t = int(input())
# # for _ in range(t):
# #   n,d,c  = map(int,input().split())
# #   graph = [[] for _ in range(n + 1)]

# #   for __ in range(d):
# #     a,b,s = map(int,input().split())
# #     graph[b].append((s, a))






# # def bfs(start):
# #   q = deque()
# #   q.append(start)
# #   visited = [False] * (n + 1)
# #   cnt = 1 
# #   while q: 
    
# #     pass