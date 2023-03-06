import sys; input = sys.stdin.readline
import math

n = input().rstrip()
min_v = math.inf
max_v = 0

def command1(n : str):
    odd_n = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_n += 1
    return odd_n

def solve(n, odd_n):
    global max_v, min_v

    if len(n) == 1:
        min_v = min(min_v, odd_n)
        max_v = max(max_v, odd_n)

    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, odd_n + command1(temp))
    else:
        for i in range(len(n) - 2):
            for j in range(i + 1, len(n) - 1):
                a = n[:i+1]
                b = n[i+1: j+1]
                c = n[j+1:]

                temp = str(int(a) + int(b) + int(c))
                solve(temp, odd_n + command1(temp))

solve(n, command1(n))
print(min_v, max_v)