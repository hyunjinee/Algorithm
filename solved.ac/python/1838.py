import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
save_arr = []
for i in range(n):
    save_arr.append([arr[i],i])
    
sorted_arr = sorted(save_arr) 
answer = [] 

for i in range(n):
    answer.append(sorted_arr[i][1] - save_arr[i][1])

print(max(answer))

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int,input().rsplit()))

# before = defaultdict(int)
# for i,num in enumerate(a):
#     before[num]=i

# a.sort()

# after = defaultdict(int)
# for i,num in enumerate(a):
#     after[num] = i

# answer = 0
# for num in before:
#     minus = before[num] - after[num]
#     if (minus > 0 and minus > answer):
#         answer = minus

# print(answer)