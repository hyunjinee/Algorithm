import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
L, C = map(int, input().split())
possible = sorted(list(input().split()))

# 최소 1개 모음 두개 자음

s = []

mo = ['a', 'e', 'i', 'o', 'u']


def dfs():

    if len(s) == L:
        mocount = 0
        jacount = 0
        for i in s:
            if i in mo:
                mocount += 1
            else:
                jacount += 1
        if mocount >= 1 and jacount >= 2:
            print(''.join(s))
            mocount = 0
            jacount = 0
            return

    for i in range(len(possible)):
        if possible[i] not in s:
            if len(s) > 0:
                if ord(s[-1]) >= ord(possible[i]):
                    continue
            s.append(possible[i])
            dfs()
            s.pop()


dfs()
