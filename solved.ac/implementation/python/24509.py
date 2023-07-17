import sys; input = sys.stdin.readline

n = int(input())
students = {}

ans = [[-1, -1] for _ in range(4)]

for i in range(n):
  number, a, b, c, d = map(int, input().split())
  score = [a, b, c, d]
  students[number] = score

for i in range(4):
  for student in students:
    if ans[i][1] < students[student][i]:
      ans[i][0] = student
      ans[i][1] = students[student][i]
    if ans[i][1] == students[student][i]:
      ans[i][0] = min(student, ans[i][0])
    
  del(students[ans[i][0]])

for i in range(4):
  print(ans[i][0], end = ' ')