import sys; input = sys.stdin.readline
n = int(input()) # 주사위의 개수
dices = [list(map(int, input().split())) for _ in range(n)]

rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

maxnum = 0
for i in range(6):
  result = [ ]
  temp = [1,2,3,4,5,6]
  temp.remove(dices[0][i])

  next = dices[0][rotate[i]]
  temp.remove(next)

  result.append(max(temp))

  for j in range(1, n):
    temp = [1,2,3,4,5,6]
    temp.remove(next)
    next = dices[j][rotate[dices[j].index(next)]]
    temp.remove(next)
    result.append(max(temp))

  result = sum(result)

  if maxnum < result:
    maxnum = result

print(maxnum)

# head = dices[0][0]
# down = dices[0][5]
# first_dice_max_side = max(dices[0][1], dices[0][2], dices[0][3], dices[0][4])

# count = 0
# temp_dice_down = head



# while count <= 6:
#   count += 1


#   sides = []
#   for idx, dice in enumerate(dices):
#     head_index = dice.index(head)
#     print(head_index)

#     if head_index == 2:
#       upper_head = dices[count][4]
#     elif head_index == 0:
#       upper_head = dices[count][5]
#     elif head_index == 1:
#       upper_head = dices[count][3]
#     elif head_index == 3:
#       upper_head = dices[count][1]
#     elif head_index == 4:
#       upper_head = dices[count][2]
#     elif head_index == 5:
#       upper_head = dices[count][0]

  
#     head = upper_head
  
#   exit()
