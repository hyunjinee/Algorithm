from collections import deque

# 입력
N = int(input())
member = [[] for _ in range(N+1)]

while True:
    mem1, mem2 = map(int, input().split())
    if mem1 == mem2 == -1:
        break
    member[mem1].append(mem2)
    member[mem2].append(mem1)
    
# 멤버별 친구관계
chon = [[51 for _ in range(N)] for _ in range(N+1)]
scores = []					# 멤버별 점수

# 멤버별로 BFS 실행
for s_mem in range(1, N+1):
    queue = deque([[s_mem, 0]])

    # BFS 시작
    while queue:
        mem, score = queue.popleft()
        chon[s_mem][mem-1] = min(chon[s_mem][mem-1], score)		# 점수 저장
        
        # 큐에 다음 친구들 추가
        mem_friends = member[mem]		
        for mf in mem_friends:
            if chon[s_mem][mf-1] == 51:		# 이미 확인한 친구들 추가 X
                queue.append([mf, score+1])

# 멤버별 점수 산정 후 저장
for i in range(1, N+1):
    scores.append(max(chon[i]))

# 회장 후보 선정
lowest_score = min(scores)
candidates = [i+1 for i in range(N) if scores[i] == lowest_score]

print(lowest_score, len(candidates), sep=' ')
print(*candidates)