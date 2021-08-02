# 2n 개를 구매 스티커를 이용해 책상을 꾸민다.


# 품질이 좋지않다. 한장을 떼면 그 스티커와 변을 공유하는 스티커느 ㄴ모두 찢어져서 활용할수 없다.


# 50 30 10 70 230

# 첫째 줄에 테스트 케이스의 개수 T가주어진다.
# dp[0][0] = arr[0][0]
# dp[1][0] = arr[1][0]



import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())

    arr = [[0] * n, [0] * n]
    dp = [[0] * n , [0] * n]

    for idx, var in enumerate(map(int,input().split())):
        arr[0][idx] = var

    for idx, var in enumerate(map(int,input().split())):
        arr[1][idx] = var

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]


    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + arr[0][i] , dp[1][i-2] + arr[0][i])
        dp[1][i] = max(dp[0][i-1] + arr[1][i] , dp[0][i-2] + arr[1][i])


    print(max(dp[0][n-1], dp[1][n-1]))