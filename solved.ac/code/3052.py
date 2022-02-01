import sys
input = sys.stdin.readline
a = [int(input()) % 42 for _ in range(10)]
a = set(a)
print(len(a))