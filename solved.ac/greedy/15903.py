# 석환이는 아기다.
# 석환이는자연수가 쓰여진 카드를 갖고 다양한 놀이를 하는 것을 좋아한다. 

# 자연수 n장을 가지고 있다.
# i 번 카드엔 ai가 써있다.

# x 번 카드와 y 번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다.
# 계산한 값을 x 번 카드와 y 번 카드 두 장 모두에 덮어쓴다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 결국 카드 두개를 골라서 합을 각각의 카드에 작성하는것인데 m 번 수행했을 때 가장 적은 점수가 나오면된다.

for i in range(m):
  cards.sort()

  temp = cards[0] + cards[1]

  cards[0] = temp
  cards[1] = temp


print(sum(cards))
