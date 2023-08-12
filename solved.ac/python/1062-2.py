import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().strip()[4: -4]) for _ in range(N)]

# K가 최소 알파벳 수보다 적으면 어떤 단어도 읽을 수 없다.
if K < 5:
    print(0)
    exit()
# 알파벳 모두를 배운다면 무조건 어떠한 단어든 다 읽을 수 있다.
if K == 26:
    print(N)
    exit()

# 단어들 중에서 겹치는 단어는 쓸모 없으므로 제거한다. set
# 배운 단어를 저장할 배열을 선언한다.
learn = [0] * 26
learn[ord('a') - ord('a')] = True
learn[ord('n') - ord('a')] = True
learn[ord('t') - ord('a')] = True
learn[ord('c') - ord('a')] = True
learn[ord('i') - ord('a')] = True
# print(learn)
# 정답을 저장할 변수를 선언합니다.
answer = 0


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
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)

print(answer)
