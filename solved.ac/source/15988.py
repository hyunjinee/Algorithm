 



t = int(input())


# n은 양수이며 백만보다 작다 일단 순차검색으로 무조건 안되고, 이게 다이나믹 프로그래밍 문제인거야



dp = [0] * 1000001



dp[1] = 1
dp[2] = 2
dp[3] = 4



for i in range(4, len(dp)):

    dp[i] = (dp[i-2] + dp[i-1] + dp[i-3]) % 1000000009



for i in range(t):


    n= int(input())



    print(dp[n])


