# 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
# 가장 ㅁ너저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한카 ㄴ이동할 수 있다면 이동
# 만약 없다면 가만히
# 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으면서 칸의 내구도가 1이상
# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료. 그렇지 않다면 1번으로 돌아간다.

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0] * n )
res = 0

while 1:
  belt.rotate(1)
  robot.rotate(1)
  robot[-1] = 0 
  if sum(robot):
    for i in range(n-2, -1, -1) :
      if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >=1:
        robot[i+1] = 1
        robot[i] = 0 
        belt[i+1] -= 1
    robot[-1] = 0 
  if robot[0] == 0 and belt[0] >= 1:
    robot[0] = 1
    belt[0] -= 1
  res += 1
  if belt.count(0) >= k:
    break

print(res)