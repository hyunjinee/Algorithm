import sys
from collections import deque
N, M = map(int, input().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 1 # 섬 고유번호
used = [] # BFS 사용시 방문여부 판단
queue = deque([]) # BFS에서 사용하는 큐(queue)
edge = [] # 생성가능한 다리 후보를 담는 배열
# BFS를 이용하여 섬 고유번호 붙이기
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    for j in range(M):
        if country[i][j] and (i, j) not in used:
            queue.append((i, j))
            used.append((i, j))
            while queue:
                r, c = queue.popleft()
                country[r][c] = cnt
                for idx in range(4):
                    nr = r + direction[idx][0]
                    nc = c + direction[idx][1]
                    if 0 <= nr < N and 0 <= nc < M:
                        if country[nr][nc] and (nr, nc) not in used:
                            queue.append((nr, nc))
                            used.append((nr, nc))
            cnt += 1


# 생성 가능한 다리 찾기
def check(li):
    start, cnt = 0, 0
    flag = False
    for idx in range(len(li)):
        if li[idx] and not flag:
            flag = True
            start = li[idx]
        elif not li[idx] and flag:
            cnt += 1
        elif li[idx] and flag and start != li[idx]:
            if start and cnt >= 2:
                if (start, li[idx], cnt) not in edge:
                    edge.append((start, li[idx], cnt))
            cnt = 0
            start = li[idx]
        elif start == li[idx]:
            cnt = 0
            


# 행 탐색
for row in country:
    if sum(row):
        check(row)

# 열 탐색
for col in list(zip(*country)):
    if sum(col):
        check(col)

# 크루스칼(Kruskal) 알고리즘 부분

edge = sorted(edge, key=lambda x:[x[2]])

parents = [i for i in range(cnt)]
rank = [1 for i in range(cnt)]

# 부모를 찾는 함수
def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

answer = 0

# 합치는 함수(grouping)
def union(v1,v2,w):
    global answer
    root1,root2 = find(v1),find(v2)

    if root1 != root2:
        answer += w

        if rank[root1] < rank[root2]:
            rank[root2] += rank[root1]
            parents[root1] = root2
        else:
            rank[root1] += rank[root2]
            parents[root2] = root1

for e in edge:
    union(e[0],e[1],e[2])

if max(rank) != cnt-1:
    print(-1)
else:
    print(answer)