"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 결혼식
description : graph
"""

from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node]+1
                queue.append(n)
    
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
check[1] = 1
bfs(1)
res = sum([1 for t in check if 2 <= t <= 3])
print(res)
# import sys
# input = sys.stdin.readline

# if __name__ == "__main__":
#     N = int(input())
#     m = int(input())
#     friend = dict()

#     for i in range(1, N+1) :
#         friend[i] = []
    
#     for _ in range(m) :
#         a, b = map(int, input().split(" "))
#         friend[a].append(b)
#         friend[b].append(a)
    
#     ans_set = set(friend[1])
#     for i in friend[1] :
#         ans_set.update(friend[i])
#     print(len(ans_set) - 1)