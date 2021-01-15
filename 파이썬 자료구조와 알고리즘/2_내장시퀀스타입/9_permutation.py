import itertools

def perm(s):
    if len(s) < 2:
        return s
    res = []

    for i,c in enumerate(s):
        for cc in perm(s[:i] + s[i+1:]):
            res.append(c+cc)

def perm2(s):
    res = itertools.permutations(s)
    
    return ["".join(i) for i in res]

print(perm2("012"))