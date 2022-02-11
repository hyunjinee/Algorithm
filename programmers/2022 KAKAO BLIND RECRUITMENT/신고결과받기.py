from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # print(id_list)
    singo_count = defaultdict(int)
    who_singo_who = defaultdict(list)
    
    for e in report :
        a,b = e.split(" ")
        if b not in who_singo_who[a]:
            who_singo_who[a].append(b)
            singo_count[b] += 1
    # print(who_singo_who)
    # print(singo_count)
    for a,b in singo_count.items():
        if b>=k :
            # a는 신고 당한사람
            # c는 신고 한사람
            for c,d in who_singo_who.items():
                if a in d:
                    idx = id_list.index(c)
                    # print(a, d, idx)
                    answer[idx] += 1
            
    return answer