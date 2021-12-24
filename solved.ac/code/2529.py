"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 부등호
description : dfs
"""

import sys
input = sys.stdin.readline
k = int(input()) #  부등호 개수
bu = input().split() # 부등호
visited = [0] * 10 # 숫자 0~9


def ok (a,b,c) : # a첫번째 숫자 b 두번째 숫자 c 부등호
  if c == '>':
    return int(a) > int(b)
  elif c == '<':
    return int(a) < int(b)

result = []

def dfs (index, s) :
  if len(s) == k + 1:
    result.append(s)
    return 
  for i in range(10):
    if not visited[i] and (index == 0 or  ok(s[-1], i,  bu[index - 1 ]) ):
      visited[i] = 1
      dfs(index + 1, s + str(i))
      visited[i] = 0



dfs(0 , "")


print(result[-1])
print(result[0])
