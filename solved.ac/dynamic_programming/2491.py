import sys;input=sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int,input().split()))
result = 1
increase = 1
decrease = 1
for i in range(1, n):
  if arr[i-1] <= arr[i]:
    increase += 1
    result = increase if increase > result else result
  else:
    increase = 1
for i in range(1, n):
  if arr[i-1] >= arr[i]:
    decrease += 1
    result = decrease if decrease > result else result 
  else: 
    decrease = 1

print(result)