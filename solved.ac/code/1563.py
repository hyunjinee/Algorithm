import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(day, late, absent):
    # 지각을 2번 or 결석 연속 3번한 경우
    if late == 2 or absent == 3:
        return 0

    # 개근을 한 경우
    if day == n:
        return 1

    if dp[day][late][absent] == -1:
        # 참석 or 지각 or 결석
        attend = (
            dfs(day + 1, late, 0)
            + dfs(day + 1, late + 1, 0)
            + dfs(day + 1, late, absent + 1)
        )
        # print(attend)
        dp[day][late][absent] = attend
        # print(day, late, absent, attend)
        return attend
    else:
        return dp[day][late][absent]


if __name__ == "__main__":
    n = int(input())
    dp = [[[-1 for absent in range(3)] for late in range(2)] for day in range(n)]
    print(dp)
    print(dfs(0, 0, 0) % 1000000)
    # print(dp)

# n = int(input())
# import sys
# sys.setrecursionlimit(10**9)
# # 지각을 두번 이상 했거나 ? 결석을 세번 연속으로 한사람은 개근상을 받을 수 없다.

# attendance = ''
# a = [ "O", "L", "A"]
# ans = 0
# def dfs(attendance, d):
#   global ans
#   # print(attendance)
#   if attendance.count("L") >= 2:
#     return
#   if len(attendance) > len(attendance.replace("AAA", "") ) :
#     return 

#   if d == n:
#     ans += 1
#     return 

#   for i in range(len(a)):
#     attendance += a[i]
#     dfs(attendance, d+1)
#     attendance = attendance[:-1]
  
# dfs(attendance, 0)

# print(ans)