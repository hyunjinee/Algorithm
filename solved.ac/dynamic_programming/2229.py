def solution(N):
    lst = list(map(int, input().split()))
    dp = [0] * N
    for i in range(1, N):
        for k in range(1, i+2):
            temp = lst[i-k+1:i+1]
            if k == i+1: k = i
            dp[i] = max(dp[i], dp[i-k] + abs(max(temp) - min(temp)))
    print(dp[-1])

if __name__ == '__main__':
    solution(int(input()))
    