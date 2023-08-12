n,m = map(int, input().split())
data = list(map(int, input().split()))
left, right = max(data), sum (data)

while left <= right:
  mid = (left + right ) // 2
  cnt =0 
  temp = 0
  for i in range(n):
    if temp + data[i] > mid :
      cnt += 1
      temp = 0
    temp += data[i]
  cnt += 1 if temp else 0
  if cnt <= m : 
    right = mid - 1
  else: 
    left = mid + 1

print(left)