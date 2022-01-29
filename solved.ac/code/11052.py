# 카드에는 등급이 있다. -> 8 가지
# 카드는 카드팩의 형태로만 구매 가능, 카드 팩의 종류는 카드1개부터 n개가 포함된 카드팩 , 총 n개의 카트팩존재
import sys
input = sys.stdin.readline
n = int(input())
# 둘째 줄에는 p1~pn까지 순서대로 주어진다. 
p = ['dummy'] + list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = p[1]
dp[2] = max(dp[1] * 2, p[2])
for i in range(3, n+1):
  for j in range(1, i+1):
    dp[i] = max(p[i], dp[i], dp[j]+dp[i-j])
print(dp[n])
# 가장 가치가 많으면서 , 가장 카드가 적게들어있는거.. 이거근데 정해진 카드의 개수가 있고 냅색해야할 거 같은데 

# knapsack = [[0 for _ in range(n+1)] for _ in range(n+1)]
