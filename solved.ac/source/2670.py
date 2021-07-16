n = int(input())


li = [float(input()) for _ in range(n)]

for i in range(1, n):
    li[i] = max(li[i], li[i] * li[i-1])

print("%.3f" % (max(li)))



