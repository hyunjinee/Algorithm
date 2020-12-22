import sys

ipt = sys.stdin.readline
arr = []

for i in range(int(ipt())):
    arr.append(int(ipt()))

arr = sorted(arr)

for i in arr:
    print(i)