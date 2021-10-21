import sys
from typing import Collection
input = sys.stdin.readline

mushroom = []

for _ in range(10):
    mushroom.append(int(input()))

score = 0
for j in mushroom:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print (score)







# print(mushroom)

# closest = [0]
# total = 0

# for i in range(0 , 10) :
#     total += mushroom[i]
#     if abs(closest[-1] - 100 ) > abs(total - 100) :
#             closest.pop()
#             closest.append(total)
#     elif abs(closest[-1] - 100) == abs(total - 100):
#             closest.append(total)
#     else: 
#         total = 0
#         continue
#     for j in range ( i + 1 , 10):
#         total += mushroom[j]
#         if abs(closest[-1] - 100 ) > abs(total - 100) :
#             closest.pop()
#             closest.append(total)
#         elif abs(closest[-1] - 100) == abs(total - 100):
#             closest.append(total)
#         else : 
#             total = 0 
#             break

# print(max(closest))

# for i in range(10):
#     if i == 9: 
#         total += mushroom[9]
#         if abs(closest[-1] - 100) > abs(total - 100):
#             closest.pop()
#             closest.append(total)
#         elif abs(closest[-1] - 100) == abs(total - 100):
#             closest.append(total)
#         break
#     total += mushroom[i]
#     for j in range(i+1, 10):
#         total += mushroom[j]

#         if abs(closest[-1] - 100) > abs(total - 100):
#             closest.pop()
#             closest.append(total)
#             break
#         elif abs(closest[-1] - 100) == abs(total - 100):
#             closest.append(total)
#             break
#     total = 0


# print(max(closest))