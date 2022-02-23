import sys
input = sys.stdin.readline

n, m = map(int, input().split())
toy = [list(input().rstrip()) for _ in range(n)]
print(toy)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

