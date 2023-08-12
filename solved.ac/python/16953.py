from collections import deque

a,b = map(int, input().split())

q = deque()
q.append([a,1])

result = -1
while q:
  x, count = q.popleft()
  if x == b:
    result = count
    break
  if x * 2 <= b:
    q.append([x*2, count+1])
  if int(str(x) + '1') <= b:
    q.append([(int(str(x)+'1')), count+1])
print(result)
