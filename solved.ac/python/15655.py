N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

s = []


def dfs():
    if len(s) == M:
        if sorted(s) == s:

            print(' '.join(map(str, s)))
            return

    else:
        for e in lst:
            if e not in s:
                s.append(e)
                dfs()
                s.pop()


dfs()
