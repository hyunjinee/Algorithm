import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input().rstrip() for _ in range(N)])

cnt = 0
for _ in range(M):
    t = input().rstrip()
    if t in s:
        cnt += 1
print(cnt)