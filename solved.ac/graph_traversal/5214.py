from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q.append(0)



n, k, m = map(int, input().split())
a = [[] for _ in range(n + m)]
c = [0 for _ in range(n + m)]
q = deque()

