n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# n = int(input())
# s = list(map(int, input().split()))
# dp = []
# dp.append(1)

# for i in range(1, n):
#     d = []
#     for j in range(i):
#         if s[i] > s[j]:
#             d.append(dp[j] + 1)
#     if not d:
#         dp.append(1)
#     else:
#         dp.append(max(d))

# print(max(dp))
