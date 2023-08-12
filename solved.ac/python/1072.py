from math import floor
import sys

input = sys.stdin.readline
x, y = map(int, input().split())
e = floor(100 * y / x)
low, high = 0, 1000000000
if e >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        tx, ty = x + mid, y + mid
        if floor(100 * ty / tx) > e:
            high = mid - 1
        else:
            low = mid + 1
    print(high + 1)
