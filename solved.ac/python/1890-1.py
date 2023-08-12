N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)]  # i,j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:  # 끝에 도달했을 때
            print(dp[i][j])
            break
        cur_cnt = field[i][j]
        # 오른쪽으로 가기
        if j + cur_cnt < N:
            dp[i][j + cur_cnt] += dp[i][j]
        # 아래로 가기
        if i + cur_cnt < N:
            dp[i + cur_cnt][j] += dp[i][j]
