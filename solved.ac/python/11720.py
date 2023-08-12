N = int(input())
numbers = []
number = input()
for i in range(len(number)):
    numbers.append(number[i])
sum = 0
for number in numbers:
    sum += int(number)
print(sum)