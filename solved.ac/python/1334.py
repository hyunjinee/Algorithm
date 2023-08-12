s = input()
n = int(len(s) / 2) 
if len(s) % 2 == 1:
  front= s[:n+1]
else: 
  front = s[:n]
next_front = front

for i in range(n-1, -1, -1) :
  next_front = next_front + next_front[i]

if int(next_front) > int(s):
  print(next_front)
else:
  next_front = str(int(front) + 1)
  if len(next_front) == len(front) :
    for i in range(n-1, -1, -1):
      next_front = next_front + next_front[i]
    print(next_front)
  else:
    print(int(s) + 2)



# n = int(input())
# listn = list(str(n))
# for digit in range(len(listn)):
#   while(True):
#     n += 10**digit
#     listn = list(str(n))
#     if(listn[digit] == listn[len(listn)-digit-1]):
#       break
#   if(listn == listn[::-1]):
#     break
# print(n)
# n = int(input())
# while True:
#   n =  n + 1
#   n = str(n)
#   start, end = 0 , len(n)  -1
#   while start < end:
#     if n[start] == n[end]:
#       start += 1
#       end -= 1
#     else: 
#       break
#     if start > end or start == end:
#       print(n)
#       exit()
#   n = int(n)
  
#   # if n == n[::-1]:
#   #   print(n)
#   #   break
  