# 출발 노드와 도착 노드를 설정, 전체 거리를 알고 싶을 때는 출발 노드만 설저하여도 무방
# 알고 있는 모든 거리 값을 부여 python 에서는 dictionary를 활용해서 graph를 표현할 수 있다.

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# 출발노드에서 시작해서 방문하지 않은 인접노드를 방문, 거리를 계산한다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
# 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면 현재 노드는 방문한 것이므로, 미방문 집합에서 제거

import heapq
def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}
  # 모든 single source shortest path problem은  초기화를 하고 시작합니다.
  distances[start] = 0 # 시작 값은 0 자기 자신의 시작값은 당연히 0 (거리)

  queue = [] # 큐를 만들고
  heapq.heappush(queue, [distances[start], start]) # 힙에 넣는다.

  while queue:
    current_distance, current_destination = heapq.heappop(queue) # 탐색할 노드의 거리, 탐색할 노드를 가져옵니다.

    if distances[current_destination] < current_distance: # 현재 그 노드까지의 최소 길이보다 그 이전의 길이가 더 길다면 그냥 넘어간다.
      continue
    # 그냥 넘어가지 않았다면 이전노드에서 탐색을 진행한다. 
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance
      if distance < distances[new_destination]:
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])
  
  return distances

print(dijkstra(graph, 'C'))