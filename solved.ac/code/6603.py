from itertools import combinations
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    s = list(combinations(s, 6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()
   # print(s)
# for i in s :
#   for j in i :
#     print(j)
# import sys
# input = sys.stdin.readline


# d = []


# def dfs(index):
#     if len(d) == 6:
#         print(*d)
#         return
#     else:
#         for i in range(index, len(s)):
#             d.append(s[i])
#             dfs(i+1)
#             d.pop()


# while True:
#     a = input().rstrip()

#     if a == '0':
#         break

#     k = int(a[0])
#     s = list(map(int, a[1:].split()))

#     for i in range(0, k - 6):
#         dfs(i)
#     print()
#     # print(k)
#     # print(s)
