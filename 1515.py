s = input()
t = input()
while s != t:
  if len(t) == 0 : print(0); exit()
  if t[-1] == 'A':
    t = t[:-1]
  elif t[-1] == 'B':
    t = t[::-1]
    t = t[1:]
print(1)

# a = input()
# b = input()
# while (b != a):
#     if (len(b) == 0):
#         print("0")
#         exit()
#     if (b[-1] == 'A'):
#         b = b[:-1]
#     elif (b[-1] == 'B'):
#         b = b[::-1]
#         b = b[1:]
#     else:
#         print("0")
#         exit()
# print("1")

# from collections import deque
# s = input()
# t = input()
# if s == t :
#   print(1)
#   exit()
# def bfs():
#   q = deque()
#   q.append(s)
#   while q: 
#     now = q.popleft()
#     if now == t:
#       print(1)
#       break
#     if len(now) > len(t):
#       print(0)
#       exit()
#     a = now[::-1] + 'B'
#     b = now + 'A'
#     q.append(a)
#     q.append(b)
# bfs()


