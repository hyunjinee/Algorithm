




# RGB 거리에는 집이 N 개 있다. 1번집의 색은 2번 집의 색과 같지 않다.
# N번 집의 색은  N-1 번의 집의 색과 같지 않아야한다.
# i 번 집의 색은 i - 1 i + 1 번의 집의 색과 같지 않아야한다.
n = int(input())



p = []

for i in range(n):
    p.append(list(map(int, input().split())))


for i in range(1, len(p)):
    p[i][0] = min(p[i-1][1], p[i-1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))