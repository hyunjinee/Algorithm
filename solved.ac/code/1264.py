import sys
input = sys.stdin.readline
# 영어 문장을 입력받아서 -> 모음의 개수 !!
mo = ['a', 'e', 'i', 'o', 'u']
while True:
  s = input().rstrip().lower()
  if s == '#':
    break
  cnt = 0 
  for alpha in s:
    if alpha in mo :
      cnt += 1
  print(cnt)