import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
team = [0] * 2000001
curmax = 1

for i in num:
    team[i] += 1
for i in range(1, 2000001):
    for j in range(i + i, 2000001, i):
        team[i] += team[j]
    if team[i] * i > team[curmax] * curmax and team[i] >= 2:
        curmax = i
print(team[curmax] * curmax)