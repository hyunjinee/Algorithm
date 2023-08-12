"""
author :  hyunjin lee
github : https://github.com/hyunjinee
e-mail : leehj0110@kakao.com

title : 거짓말
description : 그래프, union find algorithm
"""

from collections import deque
N, M = map(int, input().split())

true_list = list(map(int, input().split()))[1:]
graph = [list(map(int, input().split()))[1:] for _ in range(M)]
people = [False] * (N + 1)
party = [False] * M

for person in true_list:
    q = deque()
    q.append(person)
    people[person] = True
    while q:
        value = q.popleft()
        for i in range(len(graph)):
            if value in graph[i]:
                for j in graph[i]:
                    if not people[j]:
                        people[j] = True
                        q.append(j)
                party[i] = True


print(party.count(False))