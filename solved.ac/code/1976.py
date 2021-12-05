import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())  # 노드 수 입력 받기
M = int(input())  # 정점 수 입력 받기
parent = [0] * (N+1)  # 부모 테이블 초기화

# 부모 테이블 상에서 자기 자신을 부모로 설정
for i in range(1, N+1):
    parent[i] = i


def find(a):  # a 노드의 부모 노드 찾기
    if a == parent[a]:  # a 노드가 부모 노드이면 a 반환
        return a
    p = find(parent[a])  # a 노드를 따라가면서 부모 노드 찾기
    parent[a] = p  # 부모 테이블 갱신
    return parent[a]


def union(a, b):  # a집합과 b집합 합치기
    a = find(a)  # a 노드의 부모 노드 찾기
    b = find(b)  # b 노드의 부모 찾기

    if a == b:  # 이미 동일한 집합이면 연결시에 순환이 발생
        return

    if a < b:  # a의 부모가 b 부모보다 상위 루트이면
        parent[b] = a  # b의 부모를 a의 부모로 변경
    else:  # b의 부모가 a 부모보다 상위 루트이면
        parent[a] = b  # a의 부모 변경


for y in range(1, N+1):  # y번째 도시
    maps = list(map(int, input().split()))  # y번째 도시가 어느 도시와 연결되어 있는지 정보
    for x in range(1, len(maps)+1):  # y도시 연결 정보 추출
        if maps[x-1] == 1:  # x 도시와 연결되어 있으면
            union(y, x)  # 두 도시를 결합

tour = list(map(int, input().split()))  # 여행 계획 정보
result = set([find(i) for i in tour])  # 여행 계획의 루트 노드 찾기
if len(result) != 1:  # set 개수가 2개 이상이면 두개의 집합이 존재
    print('NO')
else:
    print('YES')  # set 개수가 1이면 한 개의 집합이 존재

# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# parent = [0] * (N + 1)
# for i in range(1, N+1):
#     parent[i] = i


# def find(a):
#     if a == parent[a]:
#         return a
#     p = find(parent[a])
#     parent[a] = p
#     return parent[a]


# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a == b:
#         return

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# for y in range(1, N+1):
#     maps = list(map(int, input().split()))
#     for x in range(1, len(maps) + 1):
#         if maps[x-1] == 1:
#             union(x, y)
# tour = list(map(int, input().split()))
# result = set([find(i) for i in tour])
# if len(result) != 1:
#     print("No")
# else:
#     print("Yes")

# for y in range(N):
#   maps = list(map(int, input().split()))
#   for x in range()

# for y in range(1, N+1):
#     maps = list(map(int, input().split()))
#     for x in range(1, len(maps) + 1):
#         if maps[x - 1] == 1:
#             union(y, x)

# # world = [list(map(int, input().split())) for _ in range(N)]
# # plan = list(map(int, input().split()))

# # # 첫째 줄에 가능하면 YES 불가능하면 NO를 출력한다.
# # # connected 되어있는가를 물어보는건데
# # # union find . 처음에는 자기 자신 노드
# # for i in range(N - 1):
# #     # if connected : continue

# #     if world[plan[i] - 1][plan[i + 1] - 1] == 1:
# #         continue
# #     else:
# #         print("NO")
# #         exit()

# # print("YES")
