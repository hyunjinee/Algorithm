"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 전쟁 - 땅따먹기
description : 구현
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  war = list(map(int, input().split()))
  people = {}
  for i in range(1, len(war)):
    if war[i] not in people:
      people[war[i]] = 1
    else :
      people[war[i]] += 1
  # print(people)

  who = 0
  ans = 0 
  for p, c in people.items():
    if ans < c:
      ans = c
      who = p
  if ans * 2 > war[0]:
    print(who)

  else :
    print("SYJKGW")
# for _ in range(int(input())):
#   war = list(map(int, input().split()))
#   size = war[0]

#   before = []
#   ans = 0
#   index = 0
#   for i in range(1, size + 1):
#     if war[i] not in before:
#       before.append((war[i], i))
#       if ans < war[1:].count(war[i]):
#         ans = war[1:].count(war[i])
#         index = i

#   if ans * 2 > size:
#     print(index)
#   else: 
#     print("SYJKGW")