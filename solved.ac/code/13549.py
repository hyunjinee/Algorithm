from collections import deque
MAX = 100001
check = [False] * MAX
dist = [-1] * MAX

n,k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 <= MAX and check[now*2] == False:  # 순간이동
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 < MAX and check[now+1] == False: # x+1이동
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and check[now-1] == False: # x-1이동
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
print(dist[k])