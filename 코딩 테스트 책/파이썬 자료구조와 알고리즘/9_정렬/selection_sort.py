def selection_sort(seq):
  length = len(seq)
  for i in range(length - 1):
    min_j = i
    for j in range(i+1, length):
      if seq[min_j] > seq[j]:
        min_j = j
    seq[i], seq[min_j] = seq[min_j], seq[i]
  return seq

