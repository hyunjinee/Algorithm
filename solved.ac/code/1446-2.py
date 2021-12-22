import sys
input = sys.stdin.readline

n, d = map(int, input().split())

roads = [list(map(int, input().split())) for _ in range(n)]

roads.sort(key=lambda x: (x[0], x[1], x[2]))
# print(roads)

distance = [i for i in range(d + 1)]

for start, end, w in roads: 
  if end <= d:
    distance[end] = min(distance[start] + w, distance[end])
  for k in range(end, d+ 1) :
    distance[k] = min(distance[k-1] + 1, distance[k])


print(distance[d])