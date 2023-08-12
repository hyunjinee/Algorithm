import sys
input = sys.stdin.readline
n,m = int(input()),int(input())
F,E = [[] for i in range(n+1)],[[] for i in range(n+1)]

def mat(s):
    if s == 'E' or s == 'F': return s
    return int(s)
def dfs(cur):
    visited[cur] = 1
    for next in F[cur]:
        if not visited[next]:
            dfs(next)
    for next1 in E[cur]:
        for next2 in E[next1]:
            if not visited[next2]:
                dfs(next2)


for i in range(m):
    r,u,v = map(mat, input().split())
    if r=='E':
        E[u] += [v]
        E[v] += [u]
    else:
        F[u] += [v]
        F[v] += [u]


visited = [0]*(n+1)
ans = 0
for i in range(1,n+1):
    if not visited[i]:
        ans+=1
        dfs(i)
print(ans)