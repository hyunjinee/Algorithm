import sys
input = sys.stdin.readline
n =int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

# 그래프로 나타내고
# 각 점에서 모든 순회점을 순회하느넫 작은 점을 찾아?