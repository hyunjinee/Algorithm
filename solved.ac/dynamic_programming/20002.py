n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1001] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i - 1][j - 1]

print(d)
ans = d[0][0]
# k: 정사각형의 한 변의 길이
for k in range(n):
    # (i, j), (i + k, j + k)를 모서리로 하는 정사각형 계산
    for i in range(1, n - k + 1):
        for j in range(1, n - k + 1):
            tmp = d[i + k][j + k] - d[i - 1][j + k] - d[i + k][j - 1] + d[i - 1][j - 1]
            ans = max(tmp, ans)
print(ans)