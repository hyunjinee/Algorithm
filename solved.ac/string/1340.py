month, d, y, t = input().split()
d = int(d[:-1])
y = int(y)
h, minute = map(int, t.split(":"))
arr = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
arr2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    arr2[1] += 1

total = sum(arr2) * 24 * 60
month_idx = arr.index(month)
current = (sum(arr2[:month_idx]) + d - 1) * 24 * 60 + h * 60 + minute
print(current / total * 100)
