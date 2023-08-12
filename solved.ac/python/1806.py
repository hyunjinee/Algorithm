
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0 , 0 
l = sys.maxsize
sum = 0
while True:
  if sum >= s:
    l = min(l , right - left)
    sum -= arr[left]
    left += 1
  elif right == n:
    break
  else:
    sum += arr[right]
    right += 1

if l == sys.maxsize :
  print(0)
else:
  print(l)