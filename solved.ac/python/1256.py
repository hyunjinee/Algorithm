import sys
input = sys.stdin.readline
 
N, M, K = map(int, input().split())
arr = [[1]*(M+1) for _ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
 
if arr[N][M] < K:
    print(-1)
else:
    result = ""
    while True:
        if N == 0 or M == 0:
            result += "z"*M
            result += "a"*N
            break
 
        flag = arr[N-1][M]
        if K <= flag:
            result += "a"
            N -= 1
        else:
            result += "z"
            M -= 1
            K -= flag
    print(result)