n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]
print(num)

# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# nums = [int(input()) for _ in range(n)]
# cnt = 0
# idx = 0
# for i in range(n):
#   if nums[i] >= k :
#     idx = i
#     break
# while idx >= 0:
#   while k-nums[idx-1] >= 0 :
#     cnt += 1
#     k -= nums[idx-1]
#   idx -= 1
#   if k == 0:
#     break

# print(cnt)

    


# # while True:

# #     while k >= 0:
# #       k -= nums[i-1]
# #       cnt += 1
# # print(cnt)