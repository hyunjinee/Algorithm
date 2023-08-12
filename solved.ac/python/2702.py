n = int(input())

# 최소 공부수와 최대공약수 출력

def gcd(a,b):
    return gcd(b%a, a) if b%a else a

for i in range(n):
    a,b = map(int, input().split())
    if a> b: a,b = b,a
    g = gcd(a,b)
    l = a * b // g

    print(l, g)

