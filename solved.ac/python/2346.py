from collections import deque
n = int(input())
q = deque(enumerate(map(int,input().split())))
ans = []
while q:
  # print(q)
  idx, num = q.popleft()
  ans.append(idx + 1)
  if num > 0:
    q.rotate(-(num -1))
  else:
    q.rotate(-num)
print(*ans)
# import sys
# input = sys.stdin.readline
# n = int(input())
# lst = list(map(int,input().split()))

# # from collections import deque

# # q = deque(lst)
# # print(q)
# cursor = 0
# bomb = lst[0] 
# cursor += int(bomb)
# lst.pop(0)
# while True:

  