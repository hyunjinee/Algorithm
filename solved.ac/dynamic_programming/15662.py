
from collections import deque
t = int(input())
topni = [deque(map(int, input())) for _ in range(t)]
topni.insert(0, [])
ans = 0
for _ in range(int(input())):
    memo = [0] * (t+1)
    n, d = map(int, input().split())
    memo[n] = d
    for i in range(n-1, 0, -1):
        if topni[i+1][6] != topni[i][2]:
            memo[i] = memo[i+1]*(-1)
    for i in range(n+1, len(topni)):
        if topni[i-1][2] != topni[i][6]:
            memo[i] = memo[i-1]*(-1)
    for i in range(1, len(topni)):
        if memo[i] == 1:
            topni[i].appendleft(topni[i].pop())
        elif memo[i] == -1:
            topni[i].append(topni[i].popleft())
for x in topni[1:]:
    if x[0] == 1:
        ans += 1
print(ans)

# import sys; input = sys.stdin.readline
# from collections import deque

# t = int(input())
# tires = [input().rstrip() for _ in range(t)]
# count = int(input())
# turns = [list(map(int, input().split())) for _ in range(count)]

# def move_left(idx, direction):
#   global curr_left, curr_right, tires
#   if idx < 0 :
#     return 
#   for i in range(idx, -1, -1):
#     if tires[i][2] != curr_left:
#       q = deque(tires[i])
#       q.rotate(direction * -1)

#       tires[idx]
#       move_left(idx - 1, direction * -1)
#     else:
#       move_left(idx - 1, direction)


# for index, direction in turns: 
#   curr_left, curr_right = tires[index - 1][6], tires[index - 1][2]
#   q = deque(tires[index - 1])
#   q.rotate(direction)

#   tires[index-1] = "".join(list(q))

#   move_left(index - 1, direction)

#   print(tires)




# # def move(n, d):
# #   global cur_left, cur_right, tires

# #   origin_dir = d

# #   for i in reversed(range(n)):
# #     if tires[i][2] != cur_left:
# #       cur_left = tires[i][6]
# #       tires[i].rotate(d *  -1)


# # for index, direction in turns:
# #   cur_left, cur_right = tires[index - 1][6], tires[index - 1][2]

# #   tires[index - 1].rotate(direction)
# #   move(index - 1, direction)


  

