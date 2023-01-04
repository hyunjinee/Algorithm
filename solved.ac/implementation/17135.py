import sys
import copy

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next

def attack(list_):
    """
    공격하기
    거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.
    - 0은 빈 칸, 1은 적
    - 거리: |r1-r2| + |c1-c2|
    :return:
    """
    # 궁수별 가까운 적 공격하기
    attack_list = list()
    cnt = 0
    for l in list_:
        pos = list()
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    now_d = abs(i - n) + abs(j - l)
                    if d >= now_d:
                        pos.append((now_d, i, j))
        pos.sort(key=(lambda x: (x[0], x[2])))  # 거리가깝고 > 왼쪽 기준 정렬
        if pos:
            attack_list.append(pos[0])   # 제거해야할 적

    for a in attack_list:
        _, i, j = a
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1
    return cnt

def move():
    """
    적 아래로 이동
    :return:
    """

    for i in range(-1, -n, -1):
        temp[i] = temp[i - 1]

    temp[0] = [0 for _ in range(m)]

def is_empty():
    """
    적 존재 유무
    :return:
    """
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True

n, m, d = map(int, sys.stdin.readline().split())  # 행, 열, 궁수의 공격 거리 제한
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
items = [i for i in range(m)]
result = 0

for a in combinations(items, 3):  # 1. 궁수 배치 - 모든 경우의 수 배치 3명
    temp = copy.deepcopy(graph)
    count = 0
    while not is_empty():  # 적이 있는 동안 계속 반복
        # 2. 적 공격하기 - 가장 가까운 적 중 왼쪽에 있는
        count += attack(a)
        # 3. 적 아래로 이동
        move()
    result = max(result, count)

print(result)