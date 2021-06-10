n = int(input())

array = list(map(int, input().split()))



d = [0] * 100




d[0] = array[0]
d[1] = max(array[0], array[1])


for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])



print(d[n-1])


# bottom up.......

# 머리가 좋으면 좋겠다. 진짜 개빡친다.




# 식량의 최대 구하려면 일단 한칸 떨어진 것 더해서 최대
# 식량창고 홀수 일때 짝수일때 다를것같은데

# 홀수면 1 1 1 ? 홀수 

