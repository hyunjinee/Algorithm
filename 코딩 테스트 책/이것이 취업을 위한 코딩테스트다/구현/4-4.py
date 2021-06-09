# a, b북쪽 서쪽으로부터 떨어진 칸의 개수
# 반시계 방향 90도부터 차례대로 갈곳 정함

# 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이
# 존재한다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감

# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어
# 있느 ㄴ경우 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 이때
# 뒤쪽 방햐잉 바다인 칸이라 뒤로 갈수 없는 경우에는 멈춘다.

n, m = map(int, input().split())


d = [[0] * m for _ in range(n)]

x,y,direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

def turn_left():

    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x =nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]


        if array[nx][ny] == 0:
            x = nx
            y = ny

        else: break
        turn_time = 0


print(count)