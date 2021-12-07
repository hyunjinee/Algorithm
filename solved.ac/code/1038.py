import sys
from itertools import combinations
input = sys.stdin.readline

N = int (input())

nums = list()

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))

nums.sort()

try:
    print(nums[N])
except:
    print(-1)
# # 음이 아닌 정수 X 의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면 그 수를 감소하는 수
# # 라고 하자.

# # n번째 감소하는 수를 출력하는 프로그램을 작성하시오.

# N = int(input())

# if N == 0 :
#     print(0)
#     exit()

# # 첫째 자리 부터 가장 작은 자리까지  내림 차순이어야겠네?
# # N번째 감소하는 수를 출력하라는거네?
# values = []
# value = 1

# def isDecreasingNumber(x):
#     x = str(x)
#     for i in range(len(x) - 1):
#         if int(x[i]) <= int(x[i+1]):
#             return False
        
#     return True


# while len(values) < N :
#     if value >= 9876543210:
#         print(-1)
#         exit()
    
#     if isDecreasingNumber(value):
#         values.append(value)
#     # print(values)
#     value += 1


# print(values[-1])