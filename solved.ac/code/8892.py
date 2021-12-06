from itertools import combinations
t = int(input())
for _ in range(t):
    k = int(input())
    words = [input() for _ in range(k)]
    combination = list(combinations(words, 2))

    for a, b in combination:
        tmp_a = a + b
        tmp_b = b + a
        if tmp_a == tmp_a[::-1]:
            print(tmp_a)
            break
        if tmp_b == tmp_b[::-1]:
            print(tmp_b)
            break
    else:
        print(0)

#
#  T = int(input())
# for _ in range(T):
#     l = []
#     k = int(input())
#     for i in range(k):
#         l.append(input())
#     flag = 0
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i != j:
#                 s = l[i] + l[j]
#                 if s == s[::-1]:
#                     print(s)
#                     flag = 1
#                     break
#                 else:
#                     continue
#         if flag == 1:
#             break

# if flag == 0:
#     print(0)
