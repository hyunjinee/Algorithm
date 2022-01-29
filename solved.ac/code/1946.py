import sys
input =sys.stdin.readline
t = int(input())
for _ in range(t):
  # 둘째 줄부터 N개의 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한줄에 주어집니다.
  n = int(input())  
  humans = sorted([list(map(int, input().split())) for _ in range(n)])
  # print(humans)
  cnt=  0
  compare = humans[0][1]
  for i in range(1,n ):
    target = humans[i][1]
    compare = min(compare, target)
    if compare < target:
      cnt += 1
  print(n - cnt)
