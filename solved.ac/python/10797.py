#7이면 7일 17일 27일에 운행하지 못한다.
# 0 이면 10일 20일 30일에 운행하지 못한다.
# 

import sys
input = sys.stdin.readline
n = int(input())
cars = list(map(int, input().split()))

print(cars.count(n))