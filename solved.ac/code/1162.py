import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

n,m,k=map(int,input().split())
arr=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
q=[[0,1,k]]
dp=[[INF]*(k+1) for i in range(n+1)]
dp[1][k]=0
while q:
    cur,x,cnt=heapq.heappop(q)
    if dp[x][cnt]<cur:
        continue
    for nx,ncur in arr[x]:
        tmp=cur+ncur
        if cnt>0:
            if cur<dp[nx][cnt-1]:
                dp[nx][cnt-1]=cur
                heapq.heappush(q,[cur,nx,cnt-1])
        if tmp<dp[nx][cnt]:
            dp[nx][cnt]=tmp
            heapq.heappush(q,[tmp,nx,cnt])
print(min(dp[n]))

# import heapq
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
# n, m, k = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# distance = [[INF for _ in range(k+1)] for _ in range(n+1)] # 도로를 몇개 포장했는지 확인하기 위해서 이중리스트로 만든다.
# for i in range(m):
#     x,y,z = map(int,input().split())
#     graph[x].append((z,y))
#     graph[y].append((z,x))

# def dijkstra(start):
#     queue = []
#     cnt = 0
#     distance[start][cnt] = 0
#     heapq.heappush(queue, (0, start, cnt))

#     while queue:
#         wei, now, cnt = heapq.heappop(queue)
#         if distance[now][cnt] < wei:
#             continue
#         for w, next_node in graph[now]:
#             next_wei = w + wei
#             if distance[next_node][cnt] > next_wei:
#                 distance[next_node][cnt] = next_wei
#                 heapq.heappush(queue, (next_wei, next_node,cnt))
                
#             # elif로 안하고 if로 하는 이유는 모든곳을 돌아 도로포장을 했을때 가장 작은 값을 찾기 위해서이다.
#             if cnt < k and distance[next_node][cnt+1] > wei: 
#             # 도로포장 횟수가 남았고 현재까지 distance[next_node][cnt+1](next_node 까지 가중치)가 wei(now 노드까지 가중치)보다 크다면 
#             # next_node까지 움직이는 w(now에서 next_node까지 가중치)를 무시하고 wei를 넣어준다.
#                 distance[next_node][cnt+1] = wei
#                 heapq.heappush(queue, (wei, next_node, cnt+1))


# dijkstra(1)
# print(min(distance[n]))
# # import sys
# # import heapq

# # input = sys.stdin.readline
# # INF = sys.maxsize
# # n,m,k = map(int,input().split())
# # graph = [[] for _ in range(n + 1)]
# # distance = [[INF for _ in range(k+1)] for _ in range(n + 1)]

# # for _ in range(m):
# #   a,b,c = map(int, input().split())
# #   graph[a].append((b,c))
# #   graph[b].append((a,c))

# # def dijkstra():
# #   q = []
# #   distance[1][0] = 0


# # # # 준영이는 매일 서울에서 포천까지 출퇴근을 ㅎ나다.
# # # # 늦잠을자서 늦게 도착한다. 
# # # # k개의 도로를 포장해 포천까지 가는 시간을 단축
# # # # n개의 도시가 주어지고 그 도로를 통과할 때 걸리는 시간이 주어졌을 때 최소시간이 걸리도록 k개이하의 도로를 포장
# # # # 도로는 이미 있는 도로만 포장할 수 있고 포장하게 되면 도로를지나는데 걸리는시간 0 
# # # # 서울 1 포천 n

# # # import sys
# # # import heapq
# # # input =sys.stdin.readline
# # # n,m,k = map(int,input().split())
# # # graph = [[] for _ in range(n+1)]

# # # for _ in range(m):
# # #   a,b,w = map(int,input().split())
# # #   graph[a].append((w, b)) 
# # #   graph[b].append((w, a))

# # # # k개 이하의 도로를 포장하여 얻을 수 있는 최소 시간을 출력해라
# # # # k개 포장하면 개이득아닌가요...??
# # # # 1-> 4로 가야하는데 최소 비용으로 가고 싶어.
# # # q = []
# # # heapq.heappush(q, (1, 0))
# # # visited = [sys.maxsize]*(n+1)
# # # visited[1] = 0

# # # while q: 
# # #   now, cost = heapq.heappop(q)
# # #   for w, next_node in graph[now]:
# # #     if visited[next_node] > cost + w:
# # #       visited[next_node] = cost + w
# # #       heapq.heappush(q, (next_node, cost + w))