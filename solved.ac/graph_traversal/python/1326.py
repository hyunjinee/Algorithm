from collections import deque

n = int(input())
bridge = [0] + list(map(int, input().split()))
start, end = map(int, input().split())


def bfs(s, e):
    q = deque([s])
    visited = [-1] * (n + 1)
    visited[s] = 0
    while q:
        now = q.popleft()
        for i in range(now, n + 1, bridge[now]): # 오른쪽 방향
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1
                if i == e:
                    return visited[i]
        for i in range(now, 0, -bridge[now]): # 왼쪽 방향
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1
                if i == e:
                    return visited[i]
    return -1 # 찾지 못한 경우


print(bfs(start, end))

# from collections import deque
# import sys; input = sys.stdin.readline


# def bfs(a,b,bridge,n):
#   q = deque()

#   q.append(a-1)
#   check=[-1]*n
#   check[a-1]=0

#   while q: 
#     node = q.popleft()

#     for i in range(n):
#       if (i - node) % bridge[node] == 0 and check[n] == -1:
#         q.append(i)

#         check[n] = check[node] + 1
#         if n == b-1:
#           return check[n]

#     return -1


# n = int(input())
# bridge = list(map(int, input().split()))

# a,b = map(int, input().split())


# print(bfs(a,b,bridge,n))