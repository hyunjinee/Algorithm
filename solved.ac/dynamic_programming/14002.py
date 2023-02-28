import sys; input = sys.stdin.readline

n = int(input())
input_array = list(map(int,input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

subsequence = []
order = max(dp)

for i in range(n - 1, - 1, -1):

  if dp[i] == order:
      subsequence.append(input_array[i])
      order -= 1

  
subsequence.reverse()
print(*subsequence)