import sys
n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
cnt = [0] * (n + 1)
for i in h:
    if cnt[i] > 0:
        cnt[i] -= 1
        cnt[i - 1] += 1
    else:
        cnt[i - 1] += 1
print(cnt)
print(sum(cnt))