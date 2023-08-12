N, M = map(int, input().split())

max_height = []
height= list(map(int, input().split()))

for i in range(max(height)):
    sumofall = 0
    for j in range(N):
        if i <= height[j]:
            sumofall += height[j] - i
    max_height.append(sumofall)

for i in range(len(max_height)):
    if max_height[i] < M:
        print(i-1)
        break

# 무조건 시간초과가 날 것이다. 애초에 숫자를 크게줬다는게 기본적으로 이딴 노가다를 쓰지말라는거
# 이걸 개선해보자