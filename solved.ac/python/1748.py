n = int(input())

count = 0

a = len(str(n))
b = n % 10

# print(a, b)

if a == 0:
    print(b)

else:
    for i in range(1, a):
        count += 10 ** (i - 1) * 9 * i
    # count += (a + 1) * (n - (10 ** a) + 1)

    count += a * (n - (10 ** (a - 1)) + 1)

print(count)
# 아래 코드는 시간 초과
# count = 0


# for i in range(1, n + 1):
#     count += len(str(i))


# print(count)
