import sys
input = sys.stdin.readline
# 없어진 숫자들의 배열에 우리가 인자로 넣은 숫자가 있으면 false 
def check (num) :
  num = list(str(num))
  for i in num:
    if i in s: return False
  return True

n = int(input())
m = int(input())
s = list(input().rstrip())
result = abs(n - 100)
for i in range(1000001):
  if check(i):
    result = min(result, len(str(i)) + abs(i - n))
print(result)