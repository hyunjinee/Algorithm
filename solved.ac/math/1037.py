count = int(input())
lst = list(map(int,input().split()))

_min = min(lst)
_max = max(lst)

print(_min * _max)