import sys
input = sys.stdin.readline

def kmp(pat, txt):
    N = len(txt)
    M = len(pat)
    lps = [0] * M
    compute_lps(pat, lps)
    
    i = 0 # index of txt
    j = 0 # index of pat
    while i < N:
        if pat[j] == txt[i]:
            if j == M - 1:
                return True
            else:
                i += 1
                j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == M:
            return True
            # 이 문제에서는 일치하는게 있는지만 검사
        

def compute_lps(pat, lps):
    leng = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1
                
if __name__ == "__main__":
    txt = input().strip()
    pat = input().strip()
    if kmp(pat, txt):
        print(1)
    else:
        print(0)