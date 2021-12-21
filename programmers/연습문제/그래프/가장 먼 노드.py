from collections import deque, defaultdict

def solution(n, edge) :
  answer = 0
  graph = defaultdict(list)
  visited= [0] * (n+1)
  for e in edge:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])
  q = deque()
  q.append(1)
  visited[1] = 1
  while q:
    l = len(q)
    for _ in range(l) :

      x = q.popleft()
      for v in graph[x]:
        if visited[v] == 0:
          q.append(v)
          visited[v] = 1
  return l
  # print(visited)


# def solution(n, edge) :
#   answer= 0 
#   graph= {}
#   visited = [0] * n
#   for e in edge:
#     graph[e[0]] = graph.get(e[0], []) + [e[1]]
#     graph[e[1]] = graph.get(e[1], []) + [e[0]]
#   # print(graph)
#   queue = deque()
#   queue.append(1)
#   visited[0] = 1
#   while queue:
#     nodes = len(queue)
#     for i in range(nodes):
#       current = queue.popleft()
#       for c in graph[current]:
#         if visited[c-1] == 0:
#           visited[c-1] = 1
#           queue.append(c)
#   return nodes


#
#  from collections import deque
# ans = 0

# def solution (n , edge) :
#   global ans
#   graph = [[0] * ( n + 1) for _ in range(n+1)]
#   visited = [0] * (n+1)
#   for a, b in edge:
#     graph[a][b] = 1
#     graph[b][a] = 1
#   q = deque()
#   q.append((1, 0))
#   count = 0
#   l = []
#   while q:
    
#     v, c =  q.popleft()
#     l.append([c])

#     visited[v] = 1

#     for i, e in enumerate(graph[v]):
#       if e == 1 and not visited[i]:
#         q.append((i, c+1))


#   print(l)
    

#   print(ans)
  # print(visited)


# ans =0 

# def solution(n, edge):
#     def dfs (x):
#         global ans
        
#         visited[x] = 1
#         print(graph[x])
#         if graph[x].count(1) == 0 :
#           ans +=1 
     

#         # print(graph[x])
        
#         for i, e in enumerate(graph[x]):
#           print(i, e)
#           if visited[i] == 0 and i != 0:
#             dfs(i)

#     graph = [[0]* (n+1) for _ in range(n+1) ]
#     visited = [0] * (n + 1)
#     for a, b in edge :
#         graph[a][b] = 1
#         # graph[b][a] = 1
#     for i in range(1,  n + 1) :
#         if not visited[i]:
#             dfs(i)
#             # print(visited)
            
    
#     print(ans)
#     return ans

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	 )
    


 