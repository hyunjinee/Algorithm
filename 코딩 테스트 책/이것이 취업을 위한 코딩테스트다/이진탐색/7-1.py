def sequential_serach(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+ 1

input_data = input().split()


n = int(input_data[0])
target = input_data[1]


array = input().split()


