import sys
input = sys.stdin.readline

n = int(input())

cards = [i for i in range(1, n+1)]

ans = []

while len(cards) > 1:
  ans.append(cards.pop(0))
  cards.append(cards.pop(0))
  # print(cards)7
  


ans.append(cards[0])

print(*ans)