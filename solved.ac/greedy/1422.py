k, n = map(int, input().split())
nums = []
for i in range(k):
    nums.append(int(input()))
max_val = max(nums)
for i in range(n-k):
    nums.append(max_val)
for i in range(n-1):
    for j in range(i+1, n):
        if int(str(nums[i])+str(nums[j])) > int(str(nums[j])+str(nums[i])):
            nums[i], nums[j] = nums[j], nums[i]
ans = ''
for i in range(n-1, -1, -1):
    ans += str(nums[i])
print(ans)