N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j] , numbers[i]

for n in numbers:
    print(n)

