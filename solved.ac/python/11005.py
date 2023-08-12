N, B = map(int, input().split())

def convert_from_decimal_larger_bases(N,B):
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result =""
    while N > 0:
        digit = N %B
        result = strings[digit] + result
        N = N // B
    return result

print(convert_from_decimal_larger_bases(N,B))


