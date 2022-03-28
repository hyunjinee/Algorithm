import sys
import math

N, L = map(int, sys.stdin.readline().split())
puddles = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
puddles.sort()

answer = 0  # 널빤지 총 개수.
pos = 0     # 현재 위치.
for puddle in puddles:
    if pos >= puddle[1]:
        continue

    if pos >= puddle[0]:
        start = pos
    else:
        start = puddle[0]

    count = math.ceil((puddle[1] - start) / L)  # 현재 추가되는 널빤지 개수.
    pos = start + count * L                     # 현재 위치 갱신.
    answer += count                             # 널빤지 총 개수 갱신.
print(answer)