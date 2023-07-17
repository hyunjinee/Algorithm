n = int(input())
move = input()
draw = [['.' for _ in range(n)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
pos = [0,0]

for i in range(len(move)):
    if move[i] == 'R':
        if pos[0] == n-1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[2]
        pos[1] += dy[2]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
            
    elif move[i] == 'L':
        if pos[0] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[0]
        pos[1] += dy[0]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '-'
        elif draw[pos[1]][pos[0]] == '|':
            draw[pos[1]][pos[0]] = '+'
            
    elif move[i] == 'U':
        if pos[1] == 0:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[3]
        pos[1] += dy[3]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
    else:
        if pos[1] == n-1:
            continue
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'
        pos[0] += dx[1]
        pos[1] += dy[1]
        if draw[pos[1]][pos[0]] == '.':
            draw[pos[1]][pos[0]] = '|'
        elif draw[pos[1]][pos[0]] == '-':
            draw[pos[1]][pos[0]] = '+'

for i in range(n):
    print(''.join(draw[i]))
# import sys; input = sys.stdin.readline


# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# n = int(input())
# arr = [['.'] * (n) for _ in range(n)]
# commands = list(input().rstrip())

# current_position = [0, 0]

# for command in commands : 
#   if command == 'D':

#   # if command == 'D':
#   #   if 0 <= current_position[0] < n and 0 <= current_position[1] < n:
#   #     if arr[current_position[1]][current_position[0]] == '-':
#   #       arr[current_position[1]][current_position[0]] = '+'
#   #     else:
#   #       arr[current_position[1]][current_position[0]] = '|'
#   #   current_position[1] += 1
#   # elif command == 'U':
#   #   if 0 <= current_position[0] < n and 0 <= current_position[1] < n:
#   #     if arr[current_position[1]][current_position[0]] == '-':
#   #       arr[current_position[1]][current_position[0]] = '+'
#   #     else:
#   #       arr[current_position[1]][current_position[0]] = '|'
#   #   current_position[1] -= 1
#   # elif command == 'R':
#   #   if 0 <= current_position[0] < n and 0 <= current_position[1] < n:
#   #     if arr[current_position[1]][current_position[0]] == '|':
#   #       arr[current_position[1]][current_position[0]] = '+'
#   #     else:
#   #       arr[current_position[1]][current_position[0]] = '-'

#   #   current_position[0] += 1
#   # elif command == 'L':
#   #   if 0 <= current_position[0] < n and 0 <= current_position[1] < n:
#   #     if arr[current_position[1]][current_position[0]] == '|':
#   #       arr[current_position[1]][current_position[0]] = '+'
#   #     else:
#   #       arr[current_position[1]][current_position[0]] = '-'
#   #   current_position[0] -= 1




# print(arr)