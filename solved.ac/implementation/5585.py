n = int(input())
n = 1000 - n

coins = [500, 100, 50, 10, 5, 1]
cnt = 0 

for coin in coins:
  if coin > n :
    continue
  
  cnt += n // coin
  # print(cnt)
  n = n % coin

print(cnt)