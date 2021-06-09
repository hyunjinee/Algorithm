# bfs 는 너비우선 탐색이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. bfs는 선입 선출 방식인 자료구조인 큐를 이용한다.




# 인접한 노드르 반복적으로 큐에넣도록 알고리즘을 작성하면 자연스럽게 먼저들어온 것이 먼저나가게ㅗ디어 가까우 ㄴ노드부터 탐색으 ㄹ진행하게된다.




# daring just dive in 


# 너비우선탐색으 ㄴ실제로 구현함에있어서 앞에서 언급한대로 deque 라이브러리르 ㄹ사용하는 것이 좋으며 탐색을 수행함에 있어서 on의 시간이 소요된다.

# 일반 적이 ㄴ경우 실제 수행시간은 DFS보다 좋은 편이라는 점까지만 추가로 기억하자



from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited = deque([start])

    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


        

