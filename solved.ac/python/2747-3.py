fb_nums =[0,1]

n = int(input())

for i in range(2,n+1):
    fb_nums.append(fb_nums[i-1]+fb_nums[i-2])
print(fb_nums[-1])