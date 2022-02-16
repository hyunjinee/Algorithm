import sys
import collections
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k, m, p = map(int, input().split())
    ind = [0] * (m + 1)
    dic = [[] for _ in range(m + 1)]
    st = [[] for _ in range(m + 1)]
    for _ in range(p):
        a, b = map(int, input().split())
        ind[b] += 1
        dic[a].append(b)

    q = collections.deque()
    for i in range(1, m + 1):
        if ind[i] == 0:
            q.append(i)
            st[i].append(1)

    while q:
        l = len(q)
        for _ in range(l):
            x = q.popleft()
            stx = max(st[x])
            if st[x].count(stx) >= 2:
                stx += 1
            for y in dic[x]:
                st[y].append(stx)
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)

    ans = max(st[m])
    if st[m].count(ans) >= 2:
        ans += 1
    print(k, ans)

# ## 9470. Strachler 순서

# import sys
# from collections import deque

# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#   k, m, p = map(int, input().split())

#   graph = [[] for _ in range(m + 1)]
#   indegree = [0] * (m + 1)

#   order = [0] * (m + 1)
#   order_max = [[0, 0] for _ in range(m + 1)]

#   for _ in range(p):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     indegree[b] += 1

#   q = deque()
#   for i in range(1, m + 1):
#     if indegree[i] == 0:
#       q.append(i)

#   while q:
#     num = q.popleft()
#     if order_max[num][1] == 1:
#       order[num] = order_max[num][0]
#     else:
#       order[num] = order_max[num][0] + 1
    
#     for i in graph[num]:
#       indegree[i] -= 1
#       if indegree[i] == 0:
#         q.append(i)
      
#       if order_max[i][0] < order[num]:
#         order_max[i][0] = order[num]
#         order_max[i][1] = 1
#       elif order_max[i][0] == order[num]:
#         order_max[i][1] += 1

#   print(k, order[m])

# # # 하천계는 유향 그래프로 나타낼 수 있다.

# # # 강은 간선으로 나타내며 
# # # 물이 흐르는 방향은 간선의 방향이 된다. 
# # # 노드는 호수나 샘처럼 강이 시작하는 곳 강이 합쳐지거나 나눠지=는고 ㅅ바다와 만나는 곳이다. 

# # # 하천계의 순서는 바다와 만나는 노드의 순서와 같다. 바다와 만나는 노드는 항상 1개이며

# # import sys
# # from collections import deque
# # input = sys.stdin.readline
# # t = int(input())
# # for _ in range(t):
# #   k,m,p = map(int, input().split())
# #   graph = [[]for _ in range(m+1)]
# #   indegree = [0] * (m+1)
# #   order = [0] * (m + 1)
# #   order_max = [[0,0] for _ in range(m+1)]

# #   for _ in range(p):
# #     a,b= map(int, input().split())
# #     graph[a].append(b)
# #     indegree[b] += 1
# #   q = deque()
# #   for i in range(1, m+1):
# #     if indegree[i] == 0:
# #       q.append(i)

# #   while q:
# #     num = q.popleft()
# #     if order_max[num][1] == 1:
# #       order[num] = order_max[num][0]
# #     else:
# #       order[num] = order_max[num][0] + 1
# #     for i in graph[num]:
# #       indegree[i] -= 1
# #       if indegree[i] == 0:
# #         q.append(i)
# #       if order_max[i][0] < order[num]:
# #         order_max[i][0] = order[num]
# #         order_max[i][1] = 1
# #       elif order_max[i][0] == order[num]:
# #         order_max[i][1] += 1
# #   print(k, order[k])


# # # import sys
# # # from collections import deque
# # # input = sys.stdin.readline
# # # t = int(input())
# # # for _ in range(t):
# # #   k,m,p = map(int, input().split())
# # #   inDegree = [0] * (m+1)
# # #   temp = [0] * (m + 1)
# # #   Strahler = 1
# # #   graph = [[] for _ in range(m+1)]
# # #   for _ in range(p):
# # #     a,b = map(int,  input().split())
# # #     graph[a].append(b)
# # #     inDegree[b] += 1
# # #     temp[b] += 1
  
# # #   q = deque()
# # #   q.append((1, Strahler))
# # #   for l in range(len(inDegree)):
# # #     if inDegree[l] == 0: 
# # #       q.append((l, Strahler))

# # #   while q: 
# # #     now, st = q.popleft()
# # #     for next in graph[now]:
# # #       if inDegree[next] == 1 and temp[next] == 1: # 진짜 1개인 경우
# # #         inDegree[next] -= 1
# # #         q.append((next, st))
# # #       elif inDegree[next] == 1: # 원래 여러개 였던 친구
# # #         inDegree[next] -= 1
# # #         q.append((next, st + 1))
# # #       else:
# # #         inDegree[next] -= 1
# # #   print(k, st)
    



# # # for i in range(t):
# # #   inDegree = [0] * (m + 1)
# # #   Strahler = 1
# # #   graph = [[] for _ in range(m+1)]
# # #   for _ in range(p):
# # #     a,b = map(int,input().split())
# # #     graph[a].append(b)
# # #     inDegree[b] += 1

# # #   q = deque()
# # #   q.append((1, Strahler))
# # #   for l in range(len(inDegree)):
# # #     if inDegree[l] == 0: 
# # #       q.append((l, Strahler))


# # #   while q:
# # #     now, st = q.popleft()
# # #     for next  in graph[now]:
# # #       inDegree[next] -= 1
# # #       if inDegree[next] == 0:
# # #         q.append((next, st + 1))
# # #   print(st)
    
