N = int(input())
a = list(map(int, input().split()))
lst = [0] * N

for i in range(N):
    count_zero = 0 
    for j in range(N):
        if a[i] == count_zero and lst[j]== 0:
            lst[j] = i+1
            break
        elif lst[j] == 0:
            count_zero += 1

print(*lst)