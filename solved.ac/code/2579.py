# 계단은 한번에 한계단 또는 두개단씩 오를 수 이싿.


# 연속된 세개의 개단 모두 밟으면 안됌
# 시작점은 계단에 포함되지 않아
# 마지막 도착 계단은 반드시 밟는다.


# 계단에 쓰여 있는 점수가 주어ㅣㅈㄹ때 이 게임에서 얻을 수 있는 총 점수의 최댓값







import sys
input = sys.stdin.readline

n = int(input())

s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())


dp[0] = s[0]
dp[1] = s[0] + s[1]

dp[2] = max(s[1]+ s[2], s[0] + s[2])


for i in range(3, n):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])


print(dp[n-1])