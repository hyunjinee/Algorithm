from collections import deque
import sys
input = sys.stdin.readline


dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x, y, dir):
  q.append([x,y, dir])
  
n = int(input())
q=  deque()
c = []