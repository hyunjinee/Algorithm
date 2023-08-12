A,B = map(int, input().split())
result = 0
max_num = max(A,B)
min_num = min(A,B)

for i in range(min_num, max_num+1):
    result += i

print(result)