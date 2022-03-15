"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 좋은수열
description : 
"""
n = int(input())

def check(s):
  for i in range(1, (len(s) // 2 + 1)):
   if s[-i:] == s[-i*2:-i]:
     return False

  return True

 
def make(number, n):
  if check(number) is False:
    return 
  if len(number) == n :
    print(number)
    exit()
  else:
    for j in range(1, 4):
      make(number + str(j), n)

make('1', n)
# 좋은 수열 중에 가장 작은 수 . 일단 좋은 수열인가 판별해야하네??
# 숫자가 123 으로만 이루어진데.
# 그러면 