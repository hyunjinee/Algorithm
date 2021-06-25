n, m = map(int, input().split())


arr = [[0] * m for _ in range(n)]

# print(arr)


for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = nums[j]


# print(arr)


count = int(input())

for i in range(count):
    a,b, c, d = map(int,input().split())

    result = 0
    for j in range(a-1, c):
        for k in range(b-1, d):
            result += arr[j][k]
    
    print(result)