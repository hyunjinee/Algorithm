import bisect, sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = [arr[0]]
for i in range(1, n):
    if(result[-1] < arr[i]):
        result.append(arr[i])
        continue
    idx = bisect.bisect_left(result, arr[i])
    result[idx] = arr[i]
print(n - len(result))