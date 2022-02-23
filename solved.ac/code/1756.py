import sys
input = sys.stdin.readline
d, n  = map(int, input().split())
oven = list(map(int,input().split()))
pizza = list(map(int, input().split() ))

for i in range(1,d ):
  oven[i] = min(oven[i], oven[i-1])

pizzaIdx = 0
depth = d - 1

for i in reversed(range(d)):
  if pizzaIdx >= len(pizza):
    print(depth + 1)
    exit()
  
  if oven[i] >= pizza[pizzaIdx]:
    pizzaIdx += 1
    depth = i
  
print(0)

# print(oven)


# pizzaIdx = 0
# depth = d - 1

# for i in reversed(range(d)):
#   print(i, 'd')
#   if pizzaIdx >= len(pizza):
#     print(depth + 1)
#     exit()
  
#   if oven[i] >= pizza[pizzaIdx]:
#     pizzaIdx += 1
#     depth = i

# print(0)