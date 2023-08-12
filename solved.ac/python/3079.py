import sys

n, m = map(int, sys.stdin.readline().split())
t = [int(sys.stdin.readline()) for _ in range(n)]

left = min(t)
answer = right = max(t) * m

while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in range(n):
        total += mid // t[i]
    if total >= m:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
print(answer)