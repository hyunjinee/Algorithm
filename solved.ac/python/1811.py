from math import inf
import sys

N, M, B = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tall = 0
ans = inf # 시간초과 방지를 위해 충분히 큰 수로 둠

for i in range(257): # 땅의 높이의 최대는 256이므로 0 ~ 256까지만 탐색
    max = 0
    min = 0
    for j in range(N): # 가로
        for k in range(M): # 세로
            if ground[j][k] < i: # 블럭이 현재 높이 보다 작다면
                min += (i - ground[j][k]) # 현재 높이가 블록 높이보다 높을 때 (min 만큼 인벤토리에서 꺼내서 채워야 함)

            else:
                max += (ground[j][k] - i) # 블록 높이가 현재 높이보다 높을 때 (max 만큼 블록이 제거 후 인벤토리에 들어감)

    inventory = max + B # 인벤토리에 있는 총 블록수 = 현재 인벤토리에 있는 블록 + max

    if inventory < min: # 전부 채울 수 없으므로 패스
        continue

    time = 2 * max + min # 블록 제거는 2초, 블록 추가는 1초
    
    if time <= ans: # 높이는 0 ~ 256 까지 오름차순으로 탐색하기 때문에 걸린 시간이 같아도 더 높은 높이가 출력 된다
        ans = time
        tall = i

print(ans, tall)

# import sys
# input = sys.stdin.readline
# n,m,b = map(int,input().split())
# minecraft = [list(map(int,input().split())) for _ in range(n)]

# #블록을 제거하는 작업은 2초가 걸리며 블록을 위에 놓는 작업은 1초가 걸리낟.
# # 땅 고르기에 걸리는 최소 시간과. 그 경우에 땅의 높이를 출력하시오 2 0 이런식으로
# time,height  = sys.maxsize, 0

# def calculate (height, land) :
#   # 뭘 반환해야하냐 ?  시간 반환하면 되는 거네
#   sum = 0 
#   for i in range(n):
#     for j in range(m):
#       if land[i][j] > height:
#         sum += (land[i][j] - height) * 2
#       else:
#         sum += (height - land[i][j]) * 1
#   return sum



# for h in range(257):
#   calculated_time = calculate(h, minecraft)
#   if calculated_time < time:
#     time = calculated_time
#     height = h

# print(time, height)


