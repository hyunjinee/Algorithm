import sys
input = sys.stdin.readline
n,m=map(int,input().split())

board = [[0]*(n+1) for _ in range(n+1)]



for _ in range(n):
    a,b=map(int,input().split())
    board[a][b]=1
    board[b][a]=1