"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com
title : 친구
description : graph
"""
# 2 친구가 되기 위해서는 한칸 건너서 연결되있으면 되는거네?
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n = int(input())
friend = [list(input().rstrip()) for _ in range(n)]

people = defaultdict(list)
for i in range(n):
  for j in range(n):
    if friend[i][j] == 'Y':

      people[i+1].append(j+1)
      people[j+1].append(i+1)

ans = []
for i in range(1, n+1):
  check = [0] * (n+1)
  q = deque([i])
  visited = [False] * (n+1)
  visited[i] = True
  check[i] = 1
  while q:
    cur = q.popleft()

    for j in people[cur]:
      if not visited[j]:
        visited[j] = True
        check[j] = check[cur] + 1
        q.append(j)
  res = sum([1 for t in check if 2 <= t <= 3])
  ans.append(res)

print(max(ans))