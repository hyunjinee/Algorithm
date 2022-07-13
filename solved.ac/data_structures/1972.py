import sys
input = sys.stdin.readline

while True:
  s = input().rstrip()
  # * 이면 종료 ㄱㄱ
  if s == '*':
    break

  # 체크하는 로직
  for d in range(1, len(s) - 1):
    # 집합을 만들고,
    check = set()
    # 
    for i in range(len(s) - d):
      pairs = s[i] + s[i + d]
      if pairs in check:
        print(s, "is NOT surprising.")
        break
      else:
        check.add(pairs)
    else:
      continue
    break
  else:
    print(s, "is surprising.")

      
    