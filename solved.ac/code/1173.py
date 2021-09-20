import sys


N, m , M , T ,R = map(int, input().split())

# 만약 운동을 N분을 할 수 없다면 ? 

# 둘중의 하나의 동작만 가능하다.

X = m 
time = 0
if X + T > M:
    print(-1)
    sys.exit()
while True:
    if N== 0: 
        break
    if X + T <= M:
        X = X + T
        N = N - 1
    else :
        X = X - R
        if X < m:
            X = m

    time = time + 1


print(time)

    # 운동을 N 분 하려고하는데 필요한 최솟값을 구해야함.



