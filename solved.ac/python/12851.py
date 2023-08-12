from collections import deque
LIMIT = 100001
n, m = map(int, input().split())
visited = [-1] * (LIMIT)
q = deque()
q.append(n)
visited[n] = 0
count = 0
while q:
  now = q.popleft()
  if now == m :
    count += 1
  for a in [now*2, now+1, now-1]:
    if 0 <= a < LIMIT:
      if visited[a] == -1 or visited[a] == visited[now] + 1:
        visited[a] = visited[now] + 1
        q.append(a)
print(visited[m])
print(count)