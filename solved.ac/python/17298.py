import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []
stack.append( 0)
for i in range(1, n ):
  while stack and a[stack[-1]] < a[i]:
    answer[stack.pop()] = a[i]
  stack.append(i)
print(*answer)
# stack.append(0)
# for i in range(1, n):
#     while stack and A[stack[-1]] < A[i]:
#         answer[stack.pop()] = A[i]
#     stack.append(i)


# print(*answer)

# import sys
# input =sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))
# head,tail = 0 , 0
# while True:
#   # lets go
#   # print (head, tail, "?")
#   head += 1
#   if tail >= n-1:
#     print(-1)
#     break
#   if head >  n-1:
#     print(-1, end = ' ')
#     tail += 1
#     head = tail
#     continue
#   # print(head, tail, '?')
#   if a[head] > a[tail]:
#     print(a[head], end = ' ')
#     tail += 1
#     head = tail 
#     continue
#   elif a[head] <= a[tail]: 
#     continue



# # for i in range(n -1 ):
# #   temp = a[i + 1:]

# #   for j in range(len(temp)):
# #     if temp[j] > a[i]:
# #       print(temp[j] , end= ' ')
# #       break
  
# # if j == len(temp) - 1:
# #     print(-1)
