A = list(map(int, input()))
B = list(map(int, input()))
arr = [0]*16
for i in range(16):
    if i % 2 == 0:
        arr[i] = A[i//2]
    else:
        arr[i] = B[i//2]
while len(arr) != 2:
    temp = []
    for i in range(len(arr)-1):
        num = (arr[i]+arr[i+1]) % 10
        temp.append(num)
    arr = temp

print(*arr, sep="")

# import sys; input = sys.stdin.readline

# a = input().strip()
# b = input().strip()
# c = ''
# for i in range(len(a)):
#   c = c + a[i] + b[i]

# print(c)
# ans = c

# while len(ans) != 2:
#   result = ''
#   for i in range(len(c)-1):
#     temp = int(c[i]) + int(c[i+1])
#     result += str(temp)[-1]
  
#   ans = result

# # print(ans)
