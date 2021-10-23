# 과일 하나먹으면 길이 1증가
# 과일 들은 일정 높이를 두고 떨어져 있으며 (1 <=   <=N)
# hi 로 과일 높이 표현
# 길이가 자신보다 작거나 같으면 과일 먹음
# 스네이크버드 처음 길이 L
# 과일의 개수 N 

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

fruit = list(map(int, input().split()))
fruit.sort()


for i in range(n) :
    if l >= fruit[i]:
        l += 1
    else : break
print(l)