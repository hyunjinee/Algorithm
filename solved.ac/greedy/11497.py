from sys import stdin

for i in range(int(stdin.readline())):
    X = int(stdin.readline())
    nums = sorted(list(map(int, stdin.readline().split())))
    level = 0
    for j in range(2, X):
        level = max(level, abs(nums[j] - nums[j - 2]))
    print(level)