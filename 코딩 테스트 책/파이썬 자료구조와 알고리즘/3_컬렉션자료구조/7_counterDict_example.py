from collections import Counter

def counter_example():
    seq1 = [1,2,3,5,1,2,5,5,2,5,1,4]
    seq_counts = Counter(seq1)
    print(seq_counts)
    seq2 = [1,2,3]
    seq_counts.update(seq2)
    print(seq_counts)
    seq3 = [1,4,3]
    for key in seq3:
        seq_counts[key] +=1
    print(seq_counts)
    seq_counts_2 = Counter(seq2)
    print(seq_counts_2)
    print(seq_counts + seq_counts_2)
    print(seq_counts - seq_counts_2)
counter_example()