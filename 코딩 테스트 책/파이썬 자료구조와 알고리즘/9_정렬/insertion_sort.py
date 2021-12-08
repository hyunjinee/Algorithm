def insertion_sort(seq):
  for i in range(1, len(seq)):
    j = i

    while j > 0 and seq[j-1] > seq[j]:
      seq[j-1], seq[j] = seq[j], seq[j-1]
      j -= 1
  return seq

def insertion_sort_rec(seq, i=None):
  if i is None:
    i = len(seq) - 1
    if i == 0:
      return i
  insertion_sort_rec(seq, i-1)
  j = i
  while j > 0 and seq[j-1] > seq[j]:
    seq[j-1], seq[j] = seq[j], seq[j-1]
    j -= 1
  return seq
