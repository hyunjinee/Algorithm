from collections import deque
n = int(input())
cards = [i for i in range(n + 1)][1:]

# q = deque()
q = deque(cards)

while q:
  if len(q) == 1:
    print(q[0])
    exit()
  q.popleft()
  q.rotate(-1)
# print(q)
# q.rotate()
# print(q)
# # q = deque(cards)
# print(cards)

# q.rotate(1)
# print(cards)