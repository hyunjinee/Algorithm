import sys
from collections import deque
input = sys.stdin.readline

a = list(map(int, input().strip()))
b = list(map(int, input().strip()))

if len(a) > len(b):
  a, b = b, a

# a가 짧은게 되도록 배치

lenA = len(a)
lenB = len(b)
lenC = lenA + lenB
a = a + [0] * lenB + [0] * lenA
b = [0] * lenA + b + [0] * lenA

# print(a)
# print(b)


def check(x,y):
  for i in range(lenC):
    if x[i] == 0 or y[i] == 0:
      continue
    if x[i] and y[i] and x[i] != y[i]:
      continue
    if x[i] and y[i] and x[i] == y[i]:
      return False
  
  return True



# a를 왼쪽으로 쭉 이동하면서 길이가 최소가 되게끔.
ans = lenA + lenB

a = deque(a)


while a[-1] == 0:
  a.pop()
  a.appendleft(0)

  print(list(a))
  print(b)
  if check(a,b):
    startIndex = 0
    endIndex = 0

    
    for i in range(lenC):
      if a[i] != 0:
        startIndex = i
        break
    
    for i in range(lenC - 1, -1, -1):
      if b[i] != 0:
        endIndex = i
        break

    if startIndex == endIndex == 0:
      continue
  
    ans = min(ans , endIndex - startIndex + 1)
  
    print(ans)
print(ans)







# l = len(a) + len(b)

# a = list(map(int,input().rstrip()))
# b = list(map(int,input().rstrip()))
# len_a = len(a)
# len_b = len(b)
# if len(a) <= len(b):
#   a = a + [0] * len_b + [0] * len_a
#   b = [0] * len_a + b + [0] * len_a
# else:
#   a = [0] * len_b + a + [0] * len_b
#   b = b + [0] * len_a + [0] * len_b

# ans = 1e9

# def check (x, y):
#   global ans
#   len_x = len(a)
#   # 순회할아이를 x라 하자.
#   x = deque(x)

#   while x[-1] == 0:
#     x.appendleft(0)
#     x.pop()
#     flag = True
#     for i in range(len_x):
#       if x[i] == 0 or y[i] == 0:
#         continue
#       if x[i] and y[i] and x[i] != y[i]:
#         continue
#       if x[i] and y[i] and x[i] == y[i]:
#         flag = False
#         break

#     if not flag:
#       continue
#     else:
#       startIndex = 0
#       endIndex = 0
#       for i in range(len_x):
#         if x[i]:
#           startIndex = i
#           break
#       for i in range(len_x - 1, -1, -1):
#         if y[i]:
#           endIndex = i
#           break
      
#       ans = min(ans, endIndex - startIndex + 1)

#   return ans
    
# if a[0]:
#   print(check(a, b))
# else:
#   print(check(b, a))




# meet = 0

# for i in range(len(a)):
#   for j in range(i + 1):
#     if a[-i + j - 1] == '2' and b[i] == '2':
#       break
  


          
      

#   # for i in range(len_x):

   
# # c = a + b



# # a = a + [0] * len(b) + [0] * len(a)
# # b = [0] * len(a) + b + [0] * len(a)

# # def begyo(x,y):
# #   pass



# print(a)

# print(b)


# # print(c)
# # print(a)

# # ans = 1e9

# # start = 0

# # for i in range(len(a)):
# #   flag = True
# #   for j in range(len(b)):
# #     if a[i] == b[j] and j == len(b) - 1:
# #       ans = min(ans, max(len(a), len(b)))
# #     elif a[i] == b[j]: 
# #       continue
# #     elif a[i] != b[j]:
# #       flag = False
# #       break
  
# # print(ans)
# # for i in range(len(b)):
# #   if b[i] != a[i]:
