import sys
from collections import defaultdict
input = sys.stdin.readline
 
tree = defaultdict(int)
cnt = 0
while True:
    name = input().rstrip()
    if name == "":
        break
    tree[name] += 1
    cnt += 1
tname = list(tree.keys())
tname.sort()
 
for n in tname:
    print("%s %.4f" % (n, tree[n]*100/cnt))


# # 생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 % 를 차지하는지 구하는 프로그램을 만들어야한다.

# # 입력은 여러줄로 이루어져있으며 한줄에 하나의 나무종이름이 주어진다ㅣ. 

# # 어떤 종이름도 30글자를 넘지 않으며 

# # 주어진 각 종의 이름을 사전 순으로 출력하고 그 종이 차지하느 ㄴ비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# cnt =0 
# trees = defaultdict(int)
# while True:
  
#   tree = input().rstrip()
#   if len(tree) == 0 : break
#   if len(tree) > 1:
#     cnt += 1
#   trees[tree] += 1
    


# for tree in sorted(trees.keys()):
#   # if cnt == 0:
#   #   print()
#   if cnt == 0 : 
#     break
#   print(tree, '%.4f' % (trees[tree]/cnt*100), sep=' ')