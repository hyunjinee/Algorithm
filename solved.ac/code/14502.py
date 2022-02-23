"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 거짓말
description : 그래프, union find algorithm
"""



# 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고한다.
# 벽을 세운다
# 벽을 세운 뒤 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.
# 벽은 세개를 세운다.
# 지도가 주어졌을 때 안전영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 벽을 어디에 세우는지 모두 다 컨트롤 할 수 없다. bfs 또는 dfs 문제일것 같다.
ans = 0 # 안전 영역의 크기

