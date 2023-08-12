def dfs(root):
    global cnt
    isTrue = False
    visit[root] = 1
    for i in range(n):
        if s[root][i] == 1 and visit[i] == 0:
            isTrue = True
            dfs(i)
    if isTrue == False:
        cnt += 1
n = int(input())
li = list(map(int, input().split()))
d = int(input())
s = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]
li_len = len(li)
cnt = 0
for i in range(li_len):
    if li[i] != -1:
        s[i][li[i]] = 1
        s[li[i]][i] = 1
    else:
        root = i
for i in range(n):
    s[i][d] = 0
    s[d][i] = 0
dfs(root)
if d == root:
    print(0)
else:
    print(cnt)