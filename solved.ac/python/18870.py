import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int,input().split()))
sortedx = sorted(set(x))


dic = {sortedx[i] : i for i in range(len(sortedx))}
# print(dic)

print(*[ dic[i] for i in x])
# for i in x:
#   s =[i]
#   for j in x:
#     if j not in s and i > j :
#       s.append(j)
  
#   print(len(s)-1 , end=' ')