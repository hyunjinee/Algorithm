table = []
for i in range(10):
    temp = list(input())
    for j in range(10):
        if temp[j] == 'O':
            temp[j] = True #True: 불 켜져있음
            continue
        temp[j] = False #False: 불 꺼져있음
    table.append(temp)
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 101

for f in range(1 << 10):
  a = []
  for i in range(10):
    a.append(table[i][:])
  cnt = 0
  for i in range(10):
    if f & (1 << i):
      cnt += 1
    


# import sys
# input = sys.stdin.readline
# bulbs = [list(input().rstrip()) for _ in range(10)]

# print(bulbs)
# for i in range(10):
#   for j in range(10):

#     pass




# def check ():
#   for i in range(10):
#     for j in range(10):
#       if bulbs[i][j] == 'O':
#         return False
#   return True