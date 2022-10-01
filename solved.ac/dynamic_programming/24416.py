import sys; input = sys.stdin.readline
n = int(input())

count = 0
def fib(n, memo = {}):
  global count
  count += 1

  if n in memo:
    return memo[n]
  elif n >= 3: 
    memo[n] = fib(n-1) + fib(n-2)

  if n == 1 or n == 2: return 1
  else: 
    return (fib(n-1, memo) + fib(n-2, memo))

a = fib(n)
b = n - 2

print(a, b)