n=int(input())
nums=[]
for _ in range(n):
    nums.append(str(input()))
for i in range(1, len(nums[0])+1):
    results=[]
    for j in range(n):
        if nums[j][-i:] in results:
            break
        else:
            results.append(nums[j][-i:])
    if len(results)==n:
        print(i)
        break

# import sys;input=sys.stdin.readline
# n = int(input())
# students = [input().rstrip() for _ in range(n)]
# l = len(students[0]) - 1


# start = l - 1
# cnt = 1
# while True:
#   temp = [ ]
#   cnt += 1
#   for i in range(n):
#     if students[i][start: l] in temp:
#       break
#     else: temp.append(students[i][start: l])
  
#   if len(temp) == n :
#     print(cnt)
#     sys.exit()

#   start = start - 1


# # while l > 0:
# #   temp = students[0][l]
# #   for i in range(len(students), 0, -1):
# #     if students[i][i]





# print(students)