
import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)
# import sys
# input = sys.stdin.readline
# n = int(input())
# a,b = map(int,input().split())
# m = int(input())
# graph = [[] for _ in range(n + 1)]























# # import sys
# # from collections import deque,defaultdict
# # input = sys.stdin.readline

# # n = int(input())
# # a,b = map(int,input().split())
# # m = int(input())

# # graph = defaultdict(list)

# # for _ in range(m):
# #   x,y = map(int, input().split())
# #   graph[x].append(y)
# #   # graph[y].append(x)
# # print(graph)

# # q = deque()
# # q.append(min(a,b))
# # count = 0 
# # while q: 
# #   print("시작")
# #   x = q.popleft()
# #   print("x값")
# #   print(graph[x], x, "x입니다.")
# #   count += 1
# #   for i in graph[x]:
# #     print("??")
# #     if i == max(a,b):
# #       print(count)
# #       exit()
# #     else:
# #       q.append(i)
# #       # print("??")

# # print(-1)


# # # parent = [i for i in range(n+1)]

# # # def find (x):
# # #   if x != parent[x]:
# # #     parent[x] = find(parent[x])
# # #   return parent[x]


# # # def union(x, y):
# # #   if find(x) != find(y):
# # #     if x > y :
# # #       parent[x] = y
# # #     else:
# # #       parent[y] = x


# # # for _ in range(m):
# # #   x, y = map(int, input().split())
# # #   union(x,y)
# # # print(parent)
# # # if find(a) != find(b):
# # #   print( -1 )
# # #   exit()



# # # g = max(a,b)
# # # count = 0
# # # while True:
# # #   if g == b :
# # #     break
# # #   g = parent[g]
# # #   count += 1

# # # print(count)