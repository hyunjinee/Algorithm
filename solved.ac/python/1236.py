n, m = map(int, input().split())


# 열과 행에 한명 이상의 경비원이 존재.
temp = []


for i in range(n):
    temp.append(input())


row = []
col = []

for i in range(n):

    row.append("X" not in temp[i])

for j in range(m):
    col.append("X" not in [temp[i][j] for i in range(n)])

print(max(sum(row), sum(col)))