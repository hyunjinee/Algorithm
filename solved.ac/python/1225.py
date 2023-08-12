



a,b = map(int, input().split())

result = 0

# for i in range(len(str(a))):
#     for j in range(len(str(b))):
#         result += int(str(a)[i]) * int(str(b)[j])

a = list(str(a))
b = list(str(b))

a = sum(map(int, a))
b = sum(map(int, b))
result = a * b
print(result)



