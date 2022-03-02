import sys
input = sys.stdin.readline
n = int(input())

nums = [ ]
for _ in range(n):
  a = input().rstrip()
  temp = ''
  for i in range(len(a)):
    if a[i] in ['1','2','3','4','5','6','7','8','9','0']:
      temp += a[i]
    else:
      if len(temp) > 0:
        nums.append(temp)
        temp = ''
  if len(temp) > 0:
    nums.append(temp)

nums = list(map(int, nums) )
nums.sort()
for num in nums :
  print(num)