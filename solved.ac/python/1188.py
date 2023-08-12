def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


n, m = map(int, input().split())
print(m - GCD(n, m))

# N, M = map(int, input().split())

# # N 명의 평론가
# # N 개의 소세지

# if N >= M:
#     print(0)


# else:
#     from math import gcd
#     a = gcd(N, M)

#     n = N // a
#     m = M // a
#     count = 1
#     cut = 0

#     # print(n, m)
#     while True:
#         cut += 1
#         n += 1

#         if n >= m:
#             break

#     print(cut * N)
#     # print(count)
#     # print(count * N)
#     # 소세지 길이는 같음
#     # 예시 1
#     # 2 , 6 일때 총 6조각을 만들어야하므로
#     # 하나의 소세지가 3조각이 되어야한다

#     # 예시 2
#     # 3개의 소세지 4명의 평론가
#     # 이때는 어떻게할까? ->

#     # 예시 3
#     # 2개의 소세지 8명의 평론가
#     # 이때는 1개의 소세지가 4개로 나뉘어질 수 있어야한다.
#     # 커팅 6회

#     # 예시 4
#     # 2개의 소세지 9명의 평론가
#     # 1개당 4.5명 ?
