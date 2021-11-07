t = int(input())

# 소인수 분해한 결과를 출력하는 프로그램을 작성하시오
def solution(n):
  temp = n
  ans = []
  for i in range(2, n+ 1):
    while n % i == 0:
      ans.append(i)
      n = n // i
  # print(ans)
  for i in range(2, temp+ 1):
    if i in ans:
      print(i, ans.count(i))

for i in range(t):
  solution(int(input()))

