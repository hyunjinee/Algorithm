# 분수 A/B
# a1,b1 = map(int, input().split())
# a2,b2 = map(int, input().split())
# b3 = b1 * b2
# a3 = b1 * a2 + a1 * b2
# visited = [0] * min(a3, b3)

# for i in range(1, min(a3, b3) + 1):
#   if a3 % i == 0 and b3 % i == 0  and visited[i] == 0:

#     a3 = a3 / i
#     b3 = b3 / i
#     for j in range(1, int(min(a3, b3))) :
#       if i ** j < len(visited):
#         visited[i ** j ] = 1

  
# print (int(a3), int(b3))

# 당연히 시간초과  O(n)
# 개선 -> 메모리 초과
# 최대공약수로 나누는 방법을 적용해야한다. 

def gcd (x, y):
  mod = x % y
  while mod > 0:
    x = y
    y = mod
    mod = x % y
  return y


a, b = map(int, input().split())
c, d = map(int, input().split())

n = gcd(a * d + c * b , b * d)
print((a*d + c*b)// n , b*d //n)
