import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())


lst = list(map(int, input().split()))
count = 0

for i in lst:
    if is_prime_number(i):
        count += 1


if 1 in lst:
    count -= 1

print(count)
