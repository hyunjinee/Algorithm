import sys
input = sys.stdin.readline

N, K = map(int, input().split())


if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()


answer = 0
words = [set(input().rstrip()) for _ in range(N)]
learn = [0] * 26

for c in ('a', 'n', 't', 'i', 'c'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global answer

    if cnt == K - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False


dfs(0, 0)

print(answer)
