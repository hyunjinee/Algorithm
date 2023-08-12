import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
d = [0 for i in range(n + 1)]
cnt = 0
def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0
for i in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
for i in range(1, n + 1):
    visit = [0 for i in range(n + 1)]
    if dfs(i):
        cnt += 1
print(cnt)