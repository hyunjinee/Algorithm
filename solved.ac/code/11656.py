s = input()

arr = []

for i in range(len(s)):
  arr.append(s[i:])
arr.sort()
for i in range(len(arr)):
  print(arr[i])