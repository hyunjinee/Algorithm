# 올바른 배열이란 5개가 정렬된것 (연속적)
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted([int(input()) for _ in range(N)])
# print(arr)

temp = []
for i in range(0, N):
    cnt = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            cnt += 1
    temp.append(cnt)

print(min(temp))

# arr = []

# continuous_len = 1

# for i in range(1, N):
#     temp = 1
#     for j in range(i, N):

#         if arr[j] - arr[j-1] == 1:
#             temp += 1
#         else:
#             continuous_len = max(continuous_len, temp)
#             break

# print(continuous_len)
# for _ in range(N):
#     arr.append(int(input()))
# arr.sort()

# ans = 10000000000

# cnt = 1
# for i in range(1, N):
#     if arr[i] - arr[i - 1] == 1:
#         cnt += 1
#     else:
#         ans = min(ans, cnt)
#         cnt = 1
#     # ans = min(ans, cnt)
# if ans > cnt:
#     ans = min(ans, cnt)


# print(5 - ans)
