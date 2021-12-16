"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 회의실 배정
description : greedy
"""
n = int(input())
s = []

for i in range(n):
  first, second = map(int, input().split())

  s.append([first, second])
s = sorted(s)
# print(s)
s = sorted(s, key=lambda x: x[1]) 
# print(s)
last = 0 
cnt = 0
for i , j in s:
  if i >= last:
    cnt += 1
    last =  j
print(cnt)