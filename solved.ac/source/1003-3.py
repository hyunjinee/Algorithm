T = int(input())
def countzero(x):
    if x==0:
        return 1
    if x==1:
        return 0
    if x>=2:
        return countzero(x-1) + countzero(x-2)
def countone(y):
    if y==0:
        return 0
    if y==1:
        return 1
    else: 
        return countone(y-1) + countone(y-2)

for i in range(T):
    n = int(input())
    print(countzero(n),countone(n))

    