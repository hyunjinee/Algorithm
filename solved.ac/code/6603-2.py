import sys
sys.setrecursionlimit(10**6)


def dfs(x, cnt):
    if cnt == 6:
        for i in range(k):
            if select[i]:
                print(a[i], end=' ')
        print()
        return

    for i in range(x, k):
        select[i] = 1
        dfs(i+1, cnt + 1)
        select[i] = 0


while True:
    a = list(map(int, input().split()))
    k = a[0]
    if k == 0:
        break
    a = a[1:]
    select = [0 for _ in range(k)]
    dfs(0, 0)
    print()


# def dfs(start, depth):
#     if depth == 6:
#         for i in range(6):
#             print(combi[i], end=' ')
#         print()
#         return

#     for i in range(start, len(s)):
#         combi[depth] = s[i]


# combi = [0 for i in range(13)]

# while True:
#     s = list(map(int, input().split()))
#     if s[0] == 0:
#         break
#     del s[0]
#     dfs(0, 0)

#     print()
