import re
N=int(input())
for _ in range(N):
    regex=re.compile('(A|B|C|D|E|F)?(A+)(F+)(C+)?(A|B|C|E|F)$')
    Text=input()
    result=regex.match(Text)
    if result:
        print("Infected!")
    else:
        print("Good")
    # cp = re.compile('[A-F]?A+F+C+[A-F]?')
    # rule = re.compile('(A|B|C|D|E|F){0,1}A+F+C+(A|B|C|D|E|F){0,1}')
# import sys

# input =sys.stdin.readline
# t = int(input())

# for _ in range(t):
#   s = input().rstrip()



#   if len(s) >= 1 :
    
#     if s.count('A') >= 1:

#       if s.count('F') >= 1:

#         if s.count('C') >= 1:

          