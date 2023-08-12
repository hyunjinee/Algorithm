K = int(input())
S = input()
l = list
for i in range(len(S)//K):
    for j in range(K):
        l.append([i][j])
