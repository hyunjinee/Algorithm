import sys
input = sys.stdin.readline

n, k = map(int ,input().split())
knapsack = [0] * (k + 1)
for _ in range(n):
  w,v =map(int,input().split())
  for j in range(k, w-1,-1):
    knapsack[j] = max(knapsack[j], knapsack[j-w] + v)
print(knapsack[-1])



# n, k = map(int , input().split())
# knapsack = [[0] for _ in range(k+1) for _ in range(n+1)]
# thing = [list(map(int, input().split())) for _ in range(n)]

# for i in range(1, n+1):
#   for j in range(1, k+1):
#     weight = thing[i][0]
#     value = thing[i][1]

#     if j < weight :
#       knapsack[i][j] = knapsack[i-1][j]
#     else:
#       knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
# print(knapsack[n][k])