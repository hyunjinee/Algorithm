import sys
input = sys.stdin.readline

n = int(input())
liquid = [int(x) for x in input().split()]
liquid.sort()

tmp = sys.maxsize
idx = [0] * 3

for i in range(n-2):
  if i > 0 and liquid[i] == liquid[i-1]:
    continue
  left, right = i + 1, n- 1

  while left < right:
    sum = liquid[i] + liquid[left] + liquid[right]
    if abs(sum) < abs(tmp):
      idx[0] = liquid[i]
      idx[1] = liquid[left]
      idx[2] = liquid[right]
      tmp =sum
    
    if sum < 0 :
      left += 1
    elif sum > 0:
      right -= 1
    else:
      print(liquid[i], liquid[left], liquid[right])
      exit()

for k in range(3):
  print(idx[k], end=' ')