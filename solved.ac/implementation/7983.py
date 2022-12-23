import sys; input = sys.stdin.readline

n = int(input())
problems = [list ( map(int, input().split()) ) for _ in range(n)]

problems.sort(key=lambda x: x[1], reverse=True)

spare_time = problems[0][1]
for i in range(n):
  spare_time = min(problems[i][1], spare_time) - problems[i][0]
print(spare_time)