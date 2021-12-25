"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 예산
description : 이분탐색
"""
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
low, high = 0, max(s)
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in s:
        if i >= mid: num += mid
        else: num += i
    if num <= m: low = mid + 1
    else: high = mid - 1
print(high)

# 시간초과 풀이
# import sys
# input = sys.stdin.readline
# n = int(input())
# p = list(map(int,input().split()))
# m = int(input())
# if sum(p) > m:
#   ma = max(p)
#   for i in range(ma, min(p), -1):
#     for j in range(len(p)):
#       if p[j] > i:
#         p[j] = i
#       else: continue
#     if sum (p) <= m:
#       break
#   print(max(p))
# else:
#   print(max(p))