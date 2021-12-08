# 세준이는0 에있고 책들도 0에있는데 책에는 원래 위치가 있다.
# 책을 ㄴ놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하세용
# 책을 모두 납두고 0으로 돌아올 필요 없고
# 세준이는 한번에 최대 M권의 책을 들 수 있다.

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 책을 한번에 M권든다 ?
book = list(map(int,input().split()))
left = []
right = []

for b in book :
  if b < 0:
    left.append(b)
  else:
    right.append(b)

distance = []

left.sort()

for i in range(len(left)// M):
  distance.append(abs(left[M*i]))
if len(left) % M > 0:
  distance.append(abs(left[(len(left)// M)* M]))
# print(distance)

right.sort(reverse= True)
# print(right)
for i in range(len(right)// M):
  distance.append(right[M*i])
  # print(distance)
if len(right) % M > 0:
  distance.append(right[(len(right)// M)* M])
# print(distance)

distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)

