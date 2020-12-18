import sys
input = sys.stdin.readline
s = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a = int(str(a)[-1])
    if a != 0:
        print(s[a][b % len(s[a])])
    else:
        print(10)