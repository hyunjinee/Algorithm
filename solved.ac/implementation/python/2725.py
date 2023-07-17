import sys
input = sys.stdin.readline

c = int(input())

def gcd(i,j):
  if j ==0:
    return i
  return gcd(j, i % j)

dp = [0 for _ in range(1001)]
dp[1] = 3
for i in range(2, 1001):
  cnt =0 
  for j in range(1, i + 1):
    if i == j:
      continue
    if gcd(i,j) == 1:
      cnt += 2

  dp[i] = dp[i-1] + cnt


for _ in range(c):
  n = int(input())
  print(dp[n])


# for _ in range(c):
#   lst = []
#   n = int(input())


#   for i in range(n+1):
#     for j in range(n+1):
#       lst.append((i, j))
#   print(lst)

#   for i in range(len(lst)):
#     for j in range(len(lst)):
#       if i != j:
