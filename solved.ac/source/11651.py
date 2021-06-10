# 좌표 n 개가 주어지고 y 좌표순으로 정렬 y좌표가 같으면 x좌표 순으로 정렬하는 프로그램을 작성하기


import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[1], x[0]))
for i in so:
    print(i[0], i[1])