import sys
input = sys.stdin.readline

N = int(input())

d = list(map(int, input().split()))
for i in range(N - 1):
    temp = sorted(list(map(int, input().split())) + d, reverse=True)
    d = temp[:N]

print(d[N-1])
