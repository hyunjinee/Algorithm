# 첫번째 링 돌려
# 나머지 링도 같이 돌아가
# 나머지 링은 첫번째 링보다 빠르게 돌아가기도 했고 느리게 돌아가기도 해


n  = int(input())



lst = list(map(int, input().split()))

# print(lst)

def gcd ( x, y) :
  while y:
    x, y = y, x % y
  return x



# 출력은 총 N-1 번

# 첫번째 한바퀴돌면 두번째 몇바퀴 도는지
for i in range(1, len(lst)):
  # print(i)
  # print(lst[0])
  # print(lst[i])

  if lst[0] % lst[i] == 0:
    print(str(lst[0] // lst[i]) + "/" + "1")  
  else :
    # print(gcd(lst[0], lst[i]))
    x = gcd(lst[0], lst[i])

    print(str(lst[0] // x) + "/" + str(lst[i] // x))
  
  # pass


