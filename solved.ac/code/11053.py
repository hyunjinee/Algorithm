import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [1] * n

for i in range(1,n ):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i], d[j]+1)
print(max(d))



"""
가장 긴 증가하는 부분 수열 -> 입력값의 크기와 범위가 달랐다. 
"""