import sys
input = sys.stdin.readline
n = int(input())
s = dict()
for i in range(n):
    a, b = map(str, input().split())
    if b == "enter": s[a] = 1
    else: del s[a]
s = sorted(s.keys(), reverse=True)
for k in s: print(k)
