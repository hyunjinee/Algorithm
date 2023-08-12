import sys
input =sys.stdin.readline
n , l = map(int,input().split())
a = list(map(int, input().split())) # 물이 세는 위치
a.sort()
cnt = 0 
temp = 0
for aa in a:
  if temp < aa:
    cnt += 1
    temp = aa + l - 1
print(cnt)
# while True:
  





# cursor = 0
# ans = 0 

# i = 0 
# coverage = 0
# while True:
#   if coverage == n :
#     break
  

#   temp = a[i]
#   temp = a[i] - 0.5
#   temp2 = a[i] + l
#   ans += 1
#   for aa in a:
#     if aa > temp2 :
#       i = a.index(aa)

#     elif aa < temp2 :
#       coverage += 1