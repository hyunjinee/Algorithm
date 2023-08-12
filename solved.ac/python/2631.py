n = int(input())
chd = []
dp = [0 for _ in range(n)]
for i in range(n):
  chd.append(int(input()))
  for j in range(i):
    if chd[j] < chd[i]:
      dp[i] = max(dp[i], dp[j])
  dp[i] += 1
print(n - max(dp))

# n = int(input())
# s = []
# dp = [0 for i in range(n)]
# for i in range(n):
#     s.append(int(input()))
# dp[0] = 1
# for i in range(1, n):
#     a = []
#     for j in range(i):
#         if s[i] > s[j]:
#             a.append(dp[j])
#     if not a:
#         dp[i] = 1
#     else:
# print(n - max(dp))
#         dp[i] = max(a) + 1

#  N = int(input())  # 아이들의 수
#     people = [int(input()) for _ in range(N)]  # 아이들 번호 순서 정보

#     # 2차원 dp
#     dp = [[0] * N for _ in range(N)]

# 	# 가장 긴 증가하는 부분수열
#     for i in range(N):
#         dp[i][i] = 1  # i를 시작점으로 설정.
#         for j in range(i + 1, N):
#             for k in range(j):
#                 if people[k] < people[j]:
#                     dp[i][j] = max(dp[i][j], dp[i][k] + 1)

#     # 가장 긴 증가하는 수열 길이 계산
#     lis = 0
#     for i in range(N):
#         lis = max(lis, max(dp[i]))

#     # 전체 길이 - 가장 긴 증가하는 부분수열
#     answer = N - lis
#     print(answer)