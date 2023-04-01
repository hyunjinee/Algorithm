from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    singo = defaultdict(int)
    who_singo = defaultdict(list)
    for e in report: 
        a, b = e.split(" ")
        
        singo[b] += 1
        if b not in who_singo[a]:
            who_singo[a].append(b)
            # print(who_singo)
        elif b in who_singo[a]:
            singo[b] -= 1
         
   
    for a in singo.keys():
        if singo[a] >= k :
            idx = 0
            for b in who_singo.keys(): 

                if a in who_singo[b]:
                    answer[idx] += 1
            
                idx += 1
    print(answer)
    return answer