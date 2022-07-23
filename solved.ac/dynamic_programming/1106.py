import sys; input = sys.stdin.readline
INF = 1e9
c, n = map(int, input().split())

data = [ ]

min_cost = [INF] * (c + 100)
min_cost[0] = 0

for _ in range(n):
  data.append(list(map(int, input().split())))

data_sort = sorted(data, key=lambda x: x[0])

for cost , cus in data_sort:
  for i in range(cus, c + 100):
    min_cost[i] = min(min_cost[i - cus] + cost, min_cost[i])

print(min(min_cost[c:]))
# for _ in range(n):
#   cost, customers = map(int, input().split())
