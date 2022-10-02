from collections import deque
import sys
input = sys.stdin.readline
def bfs(mid):
    visit[i1] = 1
    q = deque()
    q.append(i1)
    while q:
        start = q.popleft()
        if start == i2: return True
        for nx, nc in s[start]:
            if visit[nx] == 0 and mid <= nc:
                q.append(nx)
                visit[nx] = 1
    return False
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
i1, i2 = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visit = [0 for i in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid): low = mid + 1
    else: high = mid - 1
print(high)