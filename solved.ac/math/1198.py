from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for a1, a2, a3 in combinations(arr, 3):
    temp = abs(a1[0]*a2[1] + a2[0]*a3[1] + a3[0]*a1[1] - (a2[0]*a1[1] + a3[0]*a2[1] + a1[0]*a3[1])) / 2
    answer = max(answer, temp)
print(answer)
