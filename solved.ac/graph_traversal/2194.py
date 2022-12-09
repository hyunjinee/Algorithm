from collections import deque
n, m, a, b, k = map(int, input().split())
graph = [ [0]*(m+1) for _ in range(n+1) ] 
for _ in range(k):
    x, y, = map(int, input().split())
    graph[x-1][y-1] = 1
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
gx, gy = map(int, input().split())
gx, gy = gx-1, gy-1

Q = deque()
Q.append((sx,sy,0))
visited = [ [0]* (m+1) for _ in range(n+1) ]
visited[sx][sy]=1

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

while len(Q) > 0:
    x, y, dist = Q.popleft()
    if x==gx and y==gy:
        print(dist)
        exit()
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        flag=1
        if 0<=dx<n and 0<=dy<m and visited[dx][dy]==1:
            continue
        for xx in range(a):
            for yy in range(b):
                if 0 > dx+xx or dx+xx >= n or 0 > dy+yy or dy+yy >= m or graph[dx+xx][dy+yy] == 1:
                    flag=0
                    break
        if flag==1:
            visited[dx][dy]=1
            Q.append((dx,dy,dist+1))