import sys
input = sys.stdin.readline

n, m = map(int,input().split())
edge = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    edge[a-1][b-1] = 1
    edge[b-1][a-1] = 1
for k in range(n):
    edge[k][k] = 0
    for i in range(n):
        for j in range(n):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

answer = sys.maxsize
first, second = -1, -1
for i in range(n-1):
    for j in range(i+1, n):
        check = 0
        for k in range(n):
            check += min(edge[i][k], edge[j][k]) * 2
            if check >= answer:
                break
        if answer > check:
            answer = check
            first = i+1
            second = j+1
print(first, second, answer)