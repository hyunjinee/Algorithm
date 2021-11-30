# n과 m 이 주어졌을 때 아래 조건을 만족하는 길이가 M
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 중복 없이 고른다.

# numbers = [i for i in range(1, N+1)]

# print(numbers)
s = []


def dfs():
    if len(s) == M:
        if sorted(s) == s:
            print(' '.join(map(str, s)))
            return

        else:
            return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
