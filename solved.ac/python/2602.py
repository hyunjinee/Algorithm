import sys
 
input = lambda: sys.stdin.readline().rstrip()
target = input()
s1 = input()
s2 = input()
 
dp = [[[0] * 2 for _ in range(len(target))] for _ in range(len(s1))]
 
for i in range(len(s1)):
    if s1[i] == target[0]:
        dp[i][0][0] = 1
    if s2[i] == target[0]:
        dp[i][0][1] = 1
 
for i in range(len(s1)):
    for j in range(1, len(target)):
        if s1[i] == target[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]
 
        if s2[i] == target[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]
 
answer = 0
for i in range(len(s1)):
    answer += (dp[i][len(target)-1][0] + dp[i][len(target)-1][1])
 
print(answer)
