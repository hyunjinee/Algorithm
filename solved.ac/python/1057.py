# the more you seek uncomfortable the more you become comfortable
n, kim, im = map(int, input().split())
count = 0
while kim != im:
    kim -= kim // 2
    im -= im // 2
    count += 1
print(count)