n = int(input())

max_l = 0
max_list  = []

for i in range(n+1):
  result = [n, i]
  j = 0

  while True:
    a = result[j ] - result[j + 1]

    if a <= -1:
      break
    
    result.append(a)

    if max_l < len(result):
      max_l = len(result)
      max_list = result
    
    j += 1

print(max_l)

for e in max_list:
  print(e, end=' ')

# print()

# import sys; input = sys.stdin.readline
# n = int(input())

# ans = 1
# ans2 = [100]

# for i in range(1, n + 1):
#   temp = [100]
#   temp.append(i)

#   # print(temp)
#   while True:
#     if temp[-2] - temp[-1] >= 0:
#       temp.append(temp[-2] - temp[-1])
#     else:
#       if ans >= len(temp):
#         pass
#       elif ans < len(temp):
#         ans2 = temp
#       break
#   ans  = max(ans , len(temp))
# print(ans)
# print(*ans2)
