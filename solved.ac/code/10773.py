import sys
input =sys.stdin.readline
k = int(input())
# k개의 줄에 정수가 한개씩 주어진다. 
ans = []


for i in range(k):

  temp = int(input())

  if temp==0:
    ans.pop()
  else:

    ans.append(temp)

print(sum(ans))