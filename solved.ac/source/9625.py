lst = [1, 0]


n = int(input())

for i in range(n):
    temp = lst[0]
    lst[0] = lst[1]
    lst[1] = temp + lst[0]


print(lst[0], lst[1])