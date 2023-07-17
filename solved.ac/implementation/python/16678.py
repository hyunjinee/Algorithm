n = int(input())
honors = []
for _ in range(n):
  honors.append(int(input()))

max_honor = 1

action = 0 

for num in sorted(honors):
  if num >= max_honor:
    action += num - max_honor
    max_honor += 1
  
  # print(action)
print(action)