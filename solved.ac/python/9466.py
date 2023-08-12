T = int(input())
for t in range(T):
    n = int(input())
    L = [None] + list(map(int, input().split()))
    visited = [False] * (n+1)
    alone = []
    for start in range(1, n+1):
        if visited[start]:  continue
        v = start
        while not visited[v]:
            visited[v] = True
            v = L[v]
        w = start
        while w != v:
            alone.append(w)
            w = L[w]
    print(len(alone))
# from itertools import cycle
# from turtle import circle


# for _ in range(int(input())):
#   n = int(input())
#   numbers = [0] + list(map(int, input().split()))
#   visited = [0]*(n+1)
#   ans = []
#   for i in range(1, n+1):
#     if not visited[i]:
#       cycle = []
#       start = i
#       while not visited[numbers[start]]:
#         visited[numbers[start]] = 1
#         cycle.append(numbers[start])
#         start = numbers[start]
#       if len(cycle)> 0:
#         ans.append(cycle)
#   print(ans)

# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# def dfs(x):
#     global ans
#     vis[x] = True
#     cycle.append(x)
#     num = arr[x]

#     if vis[num]:
#         if num in cycle:
#             ans += cycle[cycle.index(num):]
#         return
#     else:
#         dfs(num)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = [0] + list(map(int, input().split()))
#     vis = [False] * (n + 1)
#     ans = []

#     for i in range(1, n + 1):
#         if not vis[i]:
#             cycle = []
#             dfs(i)

#     print(n - len(ans))

# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#   n = int(input())
#   students = [i  for i in range(n)]
#   parents = [0] +  list(map(int, input().split()))
#   team = []
#   ans = n 

#   def find (x):
#     if parents[x] == x:
#       return x
#     else: 
#       return find(parents[x])


#   for i in range(1, len(parents)):
#     if parents[i] == i:
#       ans -= 1
#       team.append (i)
#     else:
#       temp = [i]
#       ii = i
#       while parents[ii] not in temp:
#         temp.append(parents[ii])
#         ii = parents[ii]
#       ans -= len(temp)

#   print(ans)