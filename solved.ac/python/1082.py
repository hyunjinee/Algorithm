INF = 5001
n = int(input())
room = list(map(int, input().split()))
m = int(input())
dp = [-INF for _ in range(m+1)]
for i in range(n-1, -1, -1):
    x = room[i]
    for j in range(x, m+1):
        dp[j] = max(dp[j-x]*10+i, i, dp[j])

print(dp[m])



# n = int(input())
# p = list(map(int,input().split()))
# m = int(input())
# room_number = ''










# def decide_length():
#   for i in range(1, n+1):
#     global m
#     if (m - p[-j]) // min(p) >= length - 1 - i :


# N = int(input())
# price_list = list(map(int, input().split()))
# money = int(input())
# room_no = ''
# # 자리수를 먼저 정합니다.
# def decide_next_num():
#     for j in range(1, N+1):
#         global money
#         if (money - price_list[-j])//min(price_list) >= length-1-i:
#             money -= price_list[-j]
#             return str(N-j)
# if N >=2:
#     length = (money-min(price_list[1:]))//min(price_list) + 1
# else:
#     length = 0
# for i in range(length):
#     room_no += decide_next_num()
# if length == 0:
#     print(0)
# elif room_no == '':
#     print(0)
# elif int(room_no) == 0:
#     print(0)
# else:
#     print(room_no)

# import sys;input=sys.stdin.readline
# sys.setrecursionlimit(10**9)
# temp = []

# def dfs(start):
#   global temp

#   if start == n :
#     print(temp)



#   for idx, e in enumerate(p):
#     temp.append((idx,e))
#     dfs(start + 1)
#     temp.pop()


# dfs(1)