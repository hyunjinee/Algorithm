# a, b, c = map(int, input().split())
# # a를 b 번 곱한거를 c로 나눈 나머지를 작성하시오.

# # 아래 정답은 시간 초과 뜸
# #print(a ** b % c)

# # a를 b번 곱하고 c로 나누는거를 생각해보자
def dac(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (dac(a, b//2, c) ** 2) % c
    else:
        return ((dac(a, b//2, c) ** 2)*a) % c


a, b, c = map(int, input().split())
print(dac(a, b, c))
