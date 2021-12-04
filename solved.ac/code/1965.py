import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

ans = 0

s = []
cnt = 0


def dfs(index, cnt):
    global ans
    if index == n:
        ans = max(cnt, ans)
        return cnt
    for i in range(index, n):
        if len(s) == 0:
            s.append(boxes[i])
            dfs(i+1, cnt + 1)
            s.pop()
        elif s[-1] >= boxes[i]:
            continue

        else:
            s.append(boxes[i])
            dfs(i+1, cnt + 1)
            s.pop()


dfs(0,  cnt)
# print(n, boxes)
print(ans)
