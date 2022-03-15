import sys
num = 2000000
arr = [False, False] + [True for _ in range(num-1)]
primes = []
for i in range(2, num+1):
    if arr[i]:
        primes.append(i)
        for k in range(i+i, num, i):
            arr[k] = False
def isPrime(n):
    if n > num:
        for prime in primes:
            if prime >= n:
                break
            elif n % prime == 0:
                return False
        return True
        
    # 2000000보다 작으면 소수인지 바로 확인
    else:
        return arr[n]


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split(" "))
    s = A+B
    if s < 4:
        print("NO")
    elif s % 2 == 0:
        print("YES")

    # 홀수소수는 짝수소수(2)+홀수소수의 조합으로밖에 안됨
    # s-2가 소수인지 확인
    else:
        if isPrime(s-2):
            print("YES")
        else:
            print("NO")
# import sys
# input = sys.stdin.readline
# from itertools import combinations

# def prime_list(n):
#   sieve = [True] * n
#   m = int(n ** 0.5)
#   for i in range(2, m+1):
#     if sieve[i] == True:
#       for j in range(i+i, n , i):
#         sieve[j] = False
#   return [i for i in range(2, n) if sieve[i] == True]

# for _ in range(int(input())):
#   a,b = map(int, input().split())
#   c = a + b
#   sosu = prime_list(c)
#   for aa, bb in combinations(sosu, 2):
#     if aa + bb == c:
#       print('YES')
#       break
#   else:
#     print("NO")
  
    

# # def dfs(x,y,c,idx, sosu  ):
# #   if x + y == c:
# #     return 'YES'
# #   for i in range(idx, len(sosu)):
    

# #   return 'NO'