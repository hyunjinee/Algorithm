import sys
from itertools import combinations, permutations
input=sys.stdin.readline

board = [list(input().rstrip()) for _ in range(5)]
star = 0
starx = []
stary = []

for y in range(5):
  for x in range(5):
    if board[y][x] == '*':
      star += 1
      starx.append(x)
      stary.append(y)

answer = 987654321

for c in combinations(range(25), star):
  visited = [False for _ in range(star)]
  q = [0]

  while (len(q)):
    cur = q.pop()
    visited[cur] = True
    for index, cur_visit in enumerate(visited):
      if (index != cur and cur_visit == False):
        dx = abs(c[cur]%5 - c[index]%5)
        dy = abs(c[cur]//5 - c[index]//5)    
        if dx + dy == 1:
          q.append(index)
    
  if False in visited: continue

  for p in permutations(c, star):
    cur = 0
    for index, a in enumerate(p):
      dx = abs(a % 5 - starx[index])
      dy = abs(a // 5 - stary[index])
      cur += dx + dy
    answer = min(cur, answer)

print(answer)
#         while(len(q)):
#             cur=q.pop()
#             visited[cur]=True
#             for index, cur_visit in enumerate(visited):
#                 if(index!=cur and cur_visit==False):
#                     dx=abs(c[cur]%5 - c[index]%5)
#                     dy=abs(c[cur]//5 - c[index]//5)
#                     if(dx+dy==1):
#                         q.append(index)
#         if(False in visited):
#             continue

        
#         for p in permutations(c, numstar):
#             cur=0
#             for index, a in enumerate(p):
#                 dx=abs(a%5-starx[index])
#                 dy=abs(a//5-stary[index])
#                 cur+=dx+dy
#             answer=min(cur,answer)
    
#     return answer

# print(solution())