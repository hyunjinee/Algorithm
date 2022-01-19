import sys
input = sys.stdin.readline
n = int(input())
liquids = list(map(int ,input().split()))

l, r,  answer = 0, n-1,  sys.maxsize
ansl, ansr = 0 , 0

while l < r:
  if abs(liquids[l] + liquids[r] ) < answer :
    answer = abs(liquids[l] + liquids[r])
    ansl, ansr = liquids[l], liquids[r]
  if liquids[l] + liquids[r] < 0:
    l += 1
  else: 
    r -= 1

print(ansl, ansr)

# key = sys.maxsize
# keep = (0,0 )
# for i in range(0, n-1):
#   for j in range(i+1, n):
#     if abs(l[i] + l[j]) <= key:
#       key = abs(l[i] + l[j])
#       keep = (l[i] , l[j])

# # print(key)
# print(keep[0], keep[1])