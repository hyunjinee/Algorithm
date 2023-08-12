import sys
input = sys.stdin.readline
max_line = 0
lines = []
for i in range(5):
  a = list(input().rstrip())
  if len(a) > max_line:
    max_line = len(a)
  lines.append(a)

for line in lines:
  if len (line) < max_line:
    diff = max_line - len(line)

  for i in range(max_line-1, len(line)-1, -1):
    line.append('#')

for i in range(max_line):
  for j in range(5):
    if lines[j][i] == '#':
      continue
    print(lines[j][i], end='')