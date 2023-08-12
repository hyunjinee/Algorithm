N = int(input())
lst = []

for i in range(N):
    cmd = int(input())
    if cmd == 0 :
        if len(lst)>0:
            print(min(lst))
            lst.remove(min(lst))
        else:
            print(0)
    elif cmd > 0:
        lst.append(cmd)
