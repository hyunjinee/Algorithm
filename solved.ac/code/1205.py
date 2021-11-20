# # 내림차순
# # 같은 점수가 있을 때는 그러한 점수 등수중에 가장 작은 등수가 된다.
# # 랭킹 리스트에 올라갈 수 있는 점수의 개수 P가 주어진다.

# # n , t, p 주어짐


# n, t, p = map(int, input().split())
# lanking = []
# if n > 0:

#     lanking = list(map(int, input().split()))
# else:
#     print(1)
#     exit()

# first_len = len(lanking)

# # 둘째줄은 n 이 0보다 큰경우에만 주어짐


# left = 0
# right = len(lanking) - 1
# start = left
# while left < right:
#     if t > lanking[left]:
#         # print("a")
#         lanking.insert(left, t)
#         break
#     elif t == lanking[left]:
#         # print("b")
#         lanking.insert(left + 1, t)
#         break
#     elif t < lanking[left]:
#         # print("c")
#         left += 1
# if len(lanking) == first_len and lanking[-1] >= t:
#     print(-1)
#     exit()
# elif len(lanking) == first_len and lanking[-1] < t:
#     lanking.pop()
#     lanking.append(t)
# # print(lanking)
# print(lanking.index(t) + 1)


n, new, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new:
        print(-1)
    else:
        res = n + 1
        for i in range(n):
            if score[i] <= new:
                res = i + 1
                break
        print(res)
