visit = [[False] * 6 for _ in range(6)]
lst = [input() for _ in range(36)]
lst = [[ord(l[0]) - 65, int(l[1]) - 1] for l in lst]

visit[lst[0][0]][lst[0][1]] = True
for i in range(1, 36):
    if visit[lst[i][0]][lst[i][1]]:
        print('Invalid')
        break
    if abs((lst[i][0] - lst[i - 1][0]) * (lst[i][1] - lst[i - 1][1])) != 2:
        print('Invalid')
        break
    visit[lst[i][0]][lst[i][1]] = True
else:
    if abs((lst[35][0] - lst[0][0]) * (lst[35][1] - lst[0][1])) != 2:
        print('Invalid')
    else:
        print('Valid')