# 4개의 팀이 조별리그를 진행한다.
# 한팀은 자신을 제외한 모든 상대방과 한번씩 총 3번의 경기를 치른다.
# 경기의 승자는 승점 3점을 받고 비기는 ㄱ여우 승점 1점

import sys
input =sys.stdin.readline
a,b,c,d = input().split()

for _ in range(6):
  A,B,W,D,L = input().split()
  print(A,B,W,D,L)

  