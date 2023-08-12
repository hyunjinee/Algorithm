n = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))


res = 0
m = costs[0]
for i in range(n- 1):
    if costs[i] < m:
        m = costs[i]

    res += m* roads[i]

print(res)