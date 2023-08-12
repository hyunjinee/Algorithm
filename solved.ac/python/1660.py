import sys

input = sys.stdin.readline

n = int(input())

nums = []
num = 0
idx = 1

while num < n:
    num += (idx * (idx + 1)) // 2
    nums.append(num)
    idx += 1
# 1,3,6,10,15,21,28,36,45,55

dp = [float('inf')] * (n + 1)

for i in range(1, n + 1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break
        if num > i:
            break
        dp[i] = min(dp[i], dp[i - num] + 1)

print(dp[-1])


# for i in range(1 , n + 1):
#   for num in nums:
#     if num == i:
#       dp[i] = 1
#       break
#     if num > i :break
#     dp[i] = min(dp[i], 1+ dp[i - num])
# print(dp[n])
# n = int(input())


# dp = [1]
# i = 3
# plus = 3 :
# while dp[-1] < n:

#     dp.append(dp[-1] + plus)
#     # plus += i
#     plus += i
#     i += 1

# where = 0

# for i, e in enumerate(dp):
#     if e > n:
#         where = i - 1

# dp = dp[0: where + 1]
# ans = 0
# while True:
#     if len(dp) == 0 or n == 0:
#         break
#     if dp[-1] <= n:

#         ans += 1
#         n = n - dp[-1]

#         print(n, 'n입니다.')
#         print(dp, "dp입니다.")

#     else:
#         dp.pop()

# print(ans)
# # print(dp)
