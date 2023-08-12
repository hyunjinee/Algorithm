# 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
from itertools import combinations

n, m = map(int, input().split())
ice = list(combinations(range(1, n+1), 3))
no_mat = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    no_mat[x][y] = 1
    no_mat[y][x] = 1
ans = 0
for x in ice:
    if no_mat[x[0]][x[1]] or no_mat[x[0]][x[2]] or no_mat[x[1]][x[2]]:
        continue
    ans += 1
print(ans)