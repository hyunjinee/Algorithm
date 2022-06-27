n = int(input())
data = list(map(int, input().split()))
data.sort()

left = 0
right = len(data) - 1
 
min_value = 1e9
while left < right :
  temp = data[left] + data[right]
  min_value = min(min_value, temp)
  left += 1
  right -= 1

print(min_value)