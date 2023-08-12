"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 롤 케이크
description : 구현
"""

import sys
input = sys.stdin.readline

l = int(input())
cake = [0] * (l + 1)
n = int(input())
bang = 0
ans = 0
for i in range(n):
    start, end = map(int,input().split())
    if bang < end -start + 1:
      ans = i+1
      bang = end - start + 1
    for j in range (start, end+ 1):
      if cake[j] == 0:
        cake[j] = (i + 1)
eat = 0
ans2 = 0
for i in range(n):
  if eat < cake.count(i+ 1):
    ans2 = i+ 1
    eat = cake.count(i+ 1)
  

print(ans)
print(ans2)