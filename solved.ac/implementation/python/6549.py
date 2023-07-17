import sys; input = sys.stdin.readline

def max_size():
  max_size = 0
  stack = []

  for i in range(n):
    min_point = i
    while stack and stack[-1][0] >= rect[i]:
      h, min_point = stack.pop()
      tmp_size = h * (i - min_point)
      max_size = max(max_size, tmp_size)

    stack.append([rect[i], min_point])

  for h, point in stack:
    print(h, point)
    print((n - point) * h)
    max_size = max(max_size, (n - point) * h)
    
  return max_size

while True:
  n, *rect = map(int, input().split())
  if n == 0:
    break
  print(max_size())


# import sys; input = sys.stdin.readline
# from collections import deque

# while True:
#   rec = list(map(int, input().split()))
#   n = rec.pop(0)

#   if n == 0:
#     break

#   stack = deque()
#   answer = 0

#   for i in range(n):
#     while len(stack) != 0 and rec[stack[-1]] > rec[i]:
#       tmp = stack.pop()
#       if len(stack) == 0:
#         width = i
#       else:
#         width = i - stack[-1] - 1
#       answer = max(answer, width * rec[tmp])
#     stack.append(i)
  
#   while len(stack) != 0:
#     tmp = stack.pop()
#     if len(stack) == 0:
#       width  = n
#     else:
#       width = n - stack[-1] - 1
#     answer = max(answer, width * rec[tmp])

#   print(answer)