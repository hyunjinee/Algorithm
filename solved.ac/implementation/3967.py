def solve(k,n):
    if k==5:
        if n[1]+n[2]+n[3]+n[4] != 26:return 1
    elif k==8:
        if n[0]+n[2]+n[5]+n[7] != 26: return 1
    elif k == 11:
        if n[0] + n[3] + n[6] + n[10] != 26: return 1
        if n[7] + n[8] + n[9] + n[10] != 26: return 1
    elif k==12:
        if n[1] + n[5] + n[8] + n[11] != 26: return 1
        if n[4] + n[6] + n[9] + n[11] != 26: return 1
    return 0
def back(k,n):
    global flag,nums
    if solve(k,n) or flag: return
    if k==12:
        flag = 1
        nums = n[:]
    else:
        if nums[k]:
            n[k] = nums[k]
            back(k + 1, n)
        else:
            for i in range(1, 13):
                if not used[i]:
                    used[i] = 1
                    n[k] = i
                    back(k + 1, n)
                    n[k] = 0
                    used[i] = 0
board = [list(input()) for _ in range(5)]
pos = {(0,4):0,(1,1):1,(1,3):2,(1,5):3,(1,7):4,(2,2):5,(2,6):6,
       (3, 1): 7, (3, 3): 8, (3, 5): 9, (3, 7): 10,(4, 4): 11}
nums = [0]*12
used = [0]*13
flag = 0
for i in range(5):
    for j in range(9):
        if 'A'<=board[i][j]<='L':
            used[ord(board[i][j]) - ord('A')+1] = 1
            nums[pos[(i,j)]] = ord(board[i][j]) - ord('A')+1
back(0,[0]*12)
for key, value in pos.items():
    x,y = key
    board[x][y] = chr(nums[value]+64)
for b in board:
    print(''.join(b))