answer = 0
str1, str2 = input(), input()

#dp=[[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
dp=[[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if (str1[i-1] == str2[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)

# x = input()
# y = input()

# # 최장 공통 부분 문자열을 찾으라는건가요.

# dp = [[0] * (len(x) + 1) for _ in range(len(y) + 1)]

# x_temp = ''
# y_temp = ''

# for i in range(0, len(y)):
#   for j in range(0, len(x)):

#     if y[i] == x[j]:
#       x_temp += x[j]
#       y_temp += y[i]
#       if x_temp == y_temp:
#         dp[i][j] = dp[i-1][j-1] + 1
#       else: 
#         x_temp = ''
#         y_temp = ''

#       # 늘리고, 
#     # if y[i] == x[j] and y[i-1] == x[j - 1]:
#     else: 
#       dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

# print(dp)