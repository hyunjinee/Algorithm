n = int(input())
lst = list(map(int, input().split()))

dp = [x for x in lst]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))