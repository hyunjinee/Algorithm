# 플로이드 워셜은 모든 정점 사이의 최단 경로를 찾는 알고리즘입니다. 
# 최단 경로는 길이 순으로 구해집니다. 


# 1. 하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소비용을 없다면 INF로 배열에 값을 저장
# 2. 3중 for 문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 바꾸줍니다.

import sys
INF = sys.maxsize

def Floyd_Warshall() :
  dist = [[INF] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      dist[i][j] = a[i][j]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist
n = 4 # 정점의 개수
a = [[0,2,INF, 4], [2, 0, INF, 5], [3, INF, 0 ,INF], [INF, 2,1,0]]


dist = Floyd_Warshall()

for i in range(n):
  for j in range(n):
    print(dist[i][j], end=' ')
  print()