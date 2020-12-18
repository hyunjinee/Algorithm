from sys import stdin

arr = []
result = []
total= 0
#
for i in range(8):
    arr.append(int(stdin.readline()))
for i in range(5):
    total += max(arr)
    idx = arr.index(max(arr))
    result.append(idx+1)
    arr[idx] = 0

print(total)
print(*(sorted(result)))