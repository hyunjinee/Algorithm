# n개의 재료
# 신맛 s, 쓴맛 b

import sys
input = sys.stdin.readline
n = int(input())

sour = []
bitter = []
answer = []
def mix (sour, bitter, s, b):
  if len(sour) == 0:
    answer.append(abs(s-b))
  for i in range(len(sour)):
    stemp = s * sour[i]
    btemp = b + bitter[i]
    mix(sour[i+1:], bitter[i+1:],stemp,btemp)
    mix(sour[i+1:], bitter[i+1:],s,b)

for _ in range(n):
  s,b = map(int,input().split())
  sour.append(s)
  bitter.append(b)
for i in range(n):
  s = sour[i]
  b = bitter[i]
  mix(sour[i+1:],bitter[i+1:],s,b)

print(min(answer))
# foods = []

# for _ in range(n):
#   s,b = map(int,input().split())
#   foods.append((s,b))

# visited = [False] * n

# sour = []
# bitter = []

# diff = 999999999999


# def dfs(index, count ):
#   global diff
#   sour.append(foods[index][0])
#   bitter.append(foods[index][1])
#   suoursum = 0
#   for i in range(len(sour)):
#     suoursum += sour[i]
#   bittersum = sum(bitter)
#   if abs(suoursum - bittersum) < diff:
#     diff = abs(suoursum - bittersum)

#   if count == n:
#     return 
  
#   for i in range(n):
#     if not visited[i]:
#       visited[i] = True
#       dfs(i, count + 1)
#       visited[i] = False


# for i in range(n):
#   visited[i] = True
#   dfs(i,0)
#   visited[i] = False


# # 재료를 적어도 하나 사용

