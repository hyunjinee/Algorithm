n = int(input())
s = []
num = 0
while n > 0:
    s.append(n % 2)
    n //= 2
for i in range(len(s)):
    if s[i] == 1:
        num += 3 ** i
print(num)

# from itertools import permutations
# import sys

# input = sys.stdin.readline
# # 한개 이상의 서로 다른 3의 제곱수의 합으로 표현되는 
# # N번째로 작은 수를 구하는 프로그램을 작성하시오.
# a = int(input().rstrip())
# zegopsu = [ 3 ** i for i in range(a)]

# temp = list(permutations(zegopsu, 2))

# ans = []

# for x, y in temp:
#   if x + y in ans:
#     continue
#   else: 
#     ans.append(x + y)

# for z in [1,3,9]:
#   if z in ans:
#     continue
#   else:
#     ans.append(z)
  

# ans.sort()


# print(ans[a-1])
# # n = int(input())
# # s = []
# # num = 0
# # while n > 0:
# #     s.append(n % 2)
# #     n //= 2
# # for i in range(len(s)):
# #     if s[i] == 1:
# #         num += 3 ** i

# # print(s)
# # print(num)
