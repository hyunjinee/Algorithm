import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b,c = map( int, input().split())

ans = len(a)
for i in range(len(a)):
  a[i] -= b
for i in range(len(a)):
  if a[i] <= 0:
    continue
  else:
    if a[i] % c == 0:
      ans += a[i] // c
    else:
      ans += a[i] // c  + 1 
    # while a[i] > 0 :
    #   a[i] -= c
    #   ans += 1
print(ans)