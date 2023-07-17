import sys
input =sys.stdin.readline
s1 = list(input().rstrip())
s2 = []

m = int(input())
n = len(s1)

for i in range(m):
  command = input().rstrip()
  if command[0] == 'P':
    s1.append(command[2])
  elif command[0] == 'L' and s1 != []:
    s2.append(s1.pop())
  elif command[0] == 'D' and s2 != []:
    s1.append(s2.pop())
  elif command[0] == 'B' and s1 != []:
    s1.pop()

print("".join(s1 + list(reversed(s2))))