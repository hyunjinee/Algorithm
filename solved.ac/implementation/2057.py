import math

n = int(input())
li = [math.factorial(i) for i in range(21)]

if n == 0:
	print('NO')
else:
	for i in range(20, -1, -1):
		if n >= li[i]:
			n -= li[i]
	print('YES') if n == 0 else print('NO')
