word = input().upper()

keys = list(set(word))


arr = [] 

for key in keys:
  arr.append(word.count(key))


if arr.count(max(arr)) > 1:
  print('?')
else :
  print(keys[arr.index(max(arr))])


print(arr)
print(keys)