import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
x = 0
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()
print(-1)