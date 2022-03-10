import sys


sys.setrecursionlimit(10 ** 6)


def dfs(x):
    global ans
    visited[x] = True
    cycle.append(x)
    nx = a[x]
    if visited[nx]:
        if nx in cycle:
            ans += cycle[cycle.index(nx):]
        return
    dfs(nx)


for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(ans)
    print(n - len(ans))
