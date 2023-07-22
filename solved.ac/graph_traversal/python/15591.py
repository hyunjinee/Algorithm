import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
def bfs(start, k):
  global graph
  visited = [False] * (N+1)
  q = deque()
  q.append(start)
  count = 0
  while q:
    now = q.popleft()
    visited[now] = True
    for n_n, w in graph[now]:
      if not visited[n_n] and w >= k:
        q.append(n_n)
        count += 1
  return count
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

for _ in range(Q):
  k, v = map(int, input().split())
  print(bfs(v, k))

# import sys
# input = sys.stdin.readline
# INF = float('INF')

# # bfs 함수


# def bfs(v):
#     q = [(v, INF)]  # v번 동영상부터 시작
#     visited = [False for _ in range(N+1)]  # 이번 bfs에서 방문 여부 체크
#     visited[v] = True

#     while q:
#         nv, u = q.pop(0)  # nv: 다음 동영상, u: usado

#         # next: nv번 동영상과 연결된 다음 동영상, nextU: nv번 동영상과 next번 동영상의 usado
#         for (next, nextU) in path[nv]:
#             if visited[next]:  # 이미 방문한 동영상일 경우 continue
#                 continue

#             nextUsado = min(u, nextU)  # 현재까지 연결들의 최솟값을 기록
#             q.append((next, nextUsado))
#             # usado리스트에 v번 동영상부터 next번 동영상까지의 usado 최솟값 기록
#             usado[v][next] = nextUsado
#             visited[next] = True  # next번 동영상의 방문 여부 갱신


# if __name__ == '__main__':
#     N, Q = map(int, input().split())  # N: 동영상의 개수, Q: 질문의 개수
#     check = [False for _ in range(N+1)]  # n번 동영상 bfs 여부
#     usado = [[0 for _ in range(N+1)]
#              for _ in range(N+1)]  # n번 동영상의 각 동영상에 대한 usado 기록
#     path = [[] for _ in range(N+1)]  # 입력으로 주어지는 두 동영상 쌍의 usado

#     for _ in range(N-1):
#         p, q, r = map(int, input().split())  # 동영상 p, q와 usado에 해당하는 r
#         path[p].append((q, r))  # path에 usado 기록
#         path[q].append((p, r))

#     for _ in range(Q):
#         k, v = map(int, input().split())  # k: usado 기준, v: 동영상 번호

#         if check[v]:  # 이미 bfs를 진행한 동영상이라면
#             print(len([x for x in usado[v] if x >= k]))  # 바로 k 이상의 동영상 개수를 찾는다
#             continue

#         check[v] = True  # bfs를 진행했음을 기록하고
#         bfs(v)  # 동영상 v에 대하여 bfs 진행
#         print(len([x for x in usado[v] if x >= k]))  # k 이상의 동영상 개수를 찾는다

# # from collections import defaultdict, deque

# # def find_video(start_n, k, map_dict):
# #     queue = deque()
# #     queue.append((start_n, float('inf')))
# #     visit_list = [-1] * N
# #     visit_list[start_n] = 1
# #     count = 0

# #     while queue:
# #         pop_node, min_dist = queue.popleft()
# #         for next_n, dist in map_dict[pop_node]:
# #             if visit_list[next_n] == 1: continue
# #             if min_dist > dist:
# #                 queue.append((next_n, dist))
# #                 if dist >= k: count += 1
# #             else:
# #                 queue.append((next_n, min_dist))
# #                 if min_dist >= k: count += 1
# #             visit_list[next_n] = 1

# #     return count

# # N, Q = map(int, input().split())
# # map_dict = defaultdict(list)
# # for _ in range(N-1):
# #     p, q, r = map(int, input().split())
# #     map_dict[p-1].append((q-1, r))
# #     map_dict[q-1].append((p-1, r))
# # for _ in range(Q):
# #     k, v = map(int, input().split())
# #     print(find_video(v-1, k, map_dict))