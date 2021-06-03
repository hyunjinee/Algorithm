from collections import Counter, defaultdict

def find_dice_probabilities(S, n_faces = 6):
    if S>2*n_faces or S <2:
        return None

    cdict = Counter()
    ddict = defaultdict(list)

    for dice1 in range(1, n_faces+1):
        for dice2 in range(1, n_faces+1):
            t = [dice1, dice2]
            cdict[dice1+dice2] +=1
            ddict[dice1+dice2].append(t)
    return [cdict[S], ddict[S]]

def test():
    n_faces = 6
    S = 5

    results = find_dice_probabilities(S, n_faces)
    print(results)

test()