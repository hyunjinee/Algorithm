n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
c = 0
sum = 0
for i in a:
    sum += i * b[c]
    c += 1
print(sum)