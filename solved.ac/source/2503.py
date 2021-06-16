

# for i in range(123, 988):

#     strike_count = 0
#     ball_count = 0
#     match_count = 0

#     for j in range(n):
        
#         ans, s, b = map(int, input().split())
#         # print(ans, s,b)
#         if str(i)[0] == str(ans)[0]:
#             strike_count += 1
#         else: ball_count += 1
#         if str(i)[1] == str(ans)[1]:
#             strike_count += 1
#         else: ball_count += 1
#         if str(i)[2] == str(ans)[2]:
#             strike_count += 1
#         else: ball_count += 1


#         if s == strike_count and b == ball_count:
#             match_count += 1
#         else: break
#     if match_count == n:
#         result += 1


#  반복문 잘못씀 ㅋㅋ 아 짜증

# for i in range(n):
#     ans, s, b = map(int, input().split())
#     match_count = 0
#     for j in range(123, 988):
#         strike_count = 0
#         ball_count = 0
#         if str(j)[0] == str(ans)[0]:
#             strike_count += 1
#         else:
#             ball_count += 1
#         if str(j)[1] == str(ans)[1]:
#             strike_count += 1
#         else:
#             ball_count += 1
#         if str(j)[2] == str(ans)[2]:
#             strike_count += 1
#         else:
#             ball_count += 1

#         if s == strike_count and b == ball_count:












import sys
from itertools import permutations


n = int(input())

num = list(permutations([1,2,3,4,5,6,7,8,9], 3))


for _ in range(n):
    test, s,b = map(int, input().split())


    test = list(str(test))

    remove_cnt = 0

    for i in range(len(num)):
        s_cnt= b_cnt = 0
        i -= remove_cnt

        for j in range(3):
            test[j] = int(test[j])


            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else: b_cnt += 1

        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1


print(len(num))



