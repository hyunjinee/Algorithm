import math
n,m = map(int, input().split())
up = math.factorial(n)
down = math.factorial(m) * math.factorial(n-m)

print(up//down)