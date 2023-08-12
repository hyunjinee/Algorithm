import sys
from math import comb

read = sys.stdin.readline


def solution():
    for _ in range(n-1):
        s, e = map(int, read().split())
        edge.append([s, e])
        degree[s] += 1
        degree[e] += 1
    d = 0
    g = 0
    for e in edge:
        d += (degree[e[0]] - 1) * (degree[e[1]] - 1)

    for i in range(n + 1):
        if degree[i] >= 3:
            g += comb(degree[i], 3)

    if d == g * 3:
        ans = "DUDUDUNGA"
    else:
        ans = "D" if d > g * 3 else "G"

    print(ans)


n = int(read())

edge = []
degree = [0 for _ in range(n + 1)]
solution();