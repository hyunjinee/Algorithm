import sys; input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
left, right = 0, n - 1
ans = sys.maxsize

while left < right: 
  sum = numbers[left] + numbers[right]
  if abs(sum) < abs(ans):
    ans = sum
  
  if sum ==0 : break
  elif sum > 0 : right -= 1
  else: left += 1

print(ans)
