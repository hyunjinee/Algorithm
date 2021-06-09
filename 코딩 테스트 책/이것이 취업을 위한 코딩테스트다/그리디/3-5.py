n, k = map(int, input().split())


# 입력으로 주어지는 n은 항상 k 보다 크거나 같다.



count = 0


while True:
    if n == 1:
        break

    if n % k == 0 :
        n = n / k
        count += 1

    else:
        n = n - 1
        count += 1


print(count)