def solution(info, edges):
    answer = 0
    N = len(info)
    graph = [[] for _ in range(N)]

    for edge in edges:
        p,c = edge
        graph[p].append(c)

    stack = [(1,0,[0])]
    while stack:
        cur_sheep,cur_wolf, visited = stack.pop()
        answer = max(answer,cur_sheep)
        for cur_node in visited:
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    next_sheep = cur_sheep
                    next_wolf = cur_wolf
                    if info[next_node]:
                        next_wolf += 1
                    else:
                        next_sheep += 1
                    if next_sheep <= next_wolf:
                        continue
                    stack.append((next_sheep,next_wolf,visited + [next_node]))

    return answer