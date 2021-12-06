

import sys
from typing import Counter
input = sys.stdin.readline


def dfs(pre_word, picked):
    if picked == len(S):
        return 1
    answer = 0
    for key in counter.keys():
        if pre_word == key:
            continue
        if counter[key] == 0:
            continue
        counter[key] -= 1
        answer += dfs(key, picked+1)
        counter[key] += 1
    return answer


S = list(input().strip())
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

answer = dfs('', 0)
print(answer)
# def isLuckyString(s):
#     if len(s) == 1:
#         return True
#     for i in range(1, len(s)):
#         if s[i] != s[i-1] and s[i] != s[i+1]:
#             continue
#         else:
#             return False
#     return True


# def dfs():
#     if len(d) == len(s):

#         if isLuckyString(d):
#             print(*d)

#     for i in range(len(s)):
#         if not visited[i]:
#             visited[i] = True
#             d.append(s[i])
#             dfs()
#             d.pop()
#             visited = [False] * 10


# visited = [False] * 10

# d = []
# s = input()

# if len(s) == 1:
#     print(1)
#     exit()
