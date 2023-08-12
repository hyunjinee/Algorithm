# (r,c )
# 주사위는 윗면이 1 동쪽을 바라보는 방향이 3

# 지도가 0 이면 주사위에 복사
# 주사위가 0 이면 지도에 복사

# 지도의 각 칸에는 정수가 하나씩 쓰여져있고, 주사위를 굴렸을 때 
# 이동한 칸에쓰여있는 수가 0 이면, 주사위의 바닥면에 쓰여있는 수가 칸에 복사된다.

import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]

# 주사위의 좌표 (x, y) 명ㄹ령의 개수  k 

