import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  x, y = map(int, input().split())

  distance = y - x
  num = 1
  while True:
    if num ** 2 <= distance < (num + 1) ** 2:
      break

    num += 1

  if num ** 2 == distance :
    print(num * 2 - 1)
  elif num ** 2 < distance <= num ** 2 + num:
    print(num * 2)
  else:
    print(num * 2 + 1)