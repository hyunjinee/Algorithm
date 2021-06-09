graph = [[] for _ in range(3)]



graph[0].append((1, 7))
graph[0].append((2,5))


graph[1].append((0, 7))
graph[2].append((0, 5))



print(graph)

# DFS는 깊이 우선 탐색 알고리즘이다.

# 이 알고리즘은 특정한 경로로 탐색하다가 특정한 상황에서  최대한 깊숙이 들어가서 노드를 방문한후 다시 돌아가 다른 경로를 탐색하는 알고리즘이ㅏㄷ.


# dfs 이용하여 탐색하면 일반적으로 인접한 노드 중에서 방문하지 않으 ㄴ노드가 여러개 있으며 ㄴ번호가 낮은 순서부터 처리한다.


# one call away

# tell me something boy
# for change and
# im on the deep w
# i never meet the 
# 




def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)



# 약간 부메랑 처럼 돌아오는 느낌이 강하긴하네..


