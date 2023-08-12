# 그래프가 주어 졌을 때 모든 단절점을 구해 출력하는 프로그램을 작성하시오.
# 단절점이란 그 정점을 제거했을 때 그래프가ㅣ 두개이상 또는 그 이상으로 나누어지는 정점을 말한다.
# 즉 제거했을 때 그래프의 connected component 의 개수가 증가하는 정점을 말한다.

import sys
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# 점을 제거할 때 마다 connected component 가 증가하는지 세주면 되는 거아닌가요.
# 입력으로 주어지는 그래프는 연결 그래프가 아닐 수 도 있다.

