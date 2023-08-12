import sys
from itertools import permutations
input= sys.stdin.readline


n,  k = int(input()), int(input())

cards = [input().rstrip() for _ in range(n)]


res = set()

for per in permutations(cards, k):


    res.add(''.join(per))

print(len(res))





# 이무진 신호등

# 조명ㅇ들이 날 ㅏㅂ르게 번갈악며 비추고있지만 난아직초짜란말야
# 붉은색푸른색 그사이3초그짧은시간 노랜색ㅇ및을내는 