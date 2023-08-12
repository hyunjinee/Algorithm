n = int(input())
s = list(map(int, input().split()))
a = int(input())
sum = 0
for i in s:
    if i % a == 0:
        sum += i // a
    else:
        sum += i // a + 1
print(sum * a)