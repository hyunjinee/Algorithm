N, M = map(int, input().split())
li = [[0]*100 for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            li[i-1][j-1] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if li[i][j] > M:
            cnt += 1
print(cnt)