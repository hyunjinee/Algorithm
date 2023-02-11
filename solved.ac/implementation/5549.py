import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
arr=[]
for i in range(n):
    arr.append(list(input()))
pp = [[[0,0,0] for i in range(m+1)] for j in range(n+1)] 
# 2차원 prefix sum 문제에서는 행, 열이 한 줄씩 더 필요함!! 
for i in range(n):
    for j in range(m):
        for l in range(3):
            pp[i+1][j+1][l] = pp[i+1][j][l] +pp[i][j+1][l]- pp[i][j][l]
        if arr[i][j]=='J':
            pp[i+1][j+1][0] += 1
        elif arr[i][j]=='O':
            pp[i+1][j+1][1] +=1
        elif arr[i][j]=='I':
            pp[i+1][j+1][2] += 1
for _ in range(k):
    a, b, c, d = map(int, input().split())
    answer = [0,0,0]
    for i in range(3):
        answer[i] = pp[c][d][i]-pp[a-1][d][i] - pp[c][b-1][i] + pp[a-1][b-1][i]
    print(answer[0], answer[1], answer[2])
