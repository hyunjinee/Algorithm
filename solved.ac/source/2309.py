s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.remove(two)
s.sort()
for i in s:
    print(i)