"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 공유기 설치
description : 
"""
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
position = []
result = 0

for _ in range(n):
  position.append(int(input()))
position.sort()

def counter (distance) :
  cnt = 1
  curr_p = position[0]
  for i in range(1, n ):
    if curr_p + distance <= position[i]:
      cnt += 1
      curr_p = position[i]
  return cnt


l,r = 0, position[-1] - position[0]

while l <= r:
  mid = (l + r) // 2
  if counter(mid) >= c:
    result = max(result, mid)
    l = mid + 1
  else: 
    r = mid -1
print(result)