def bubble_sort(seq):
  length = len(seq) - 1
  for num in range(length, 0, -1):
    for i in range(num):
      if seq[i] > seq[i+1]:
        seq[i], seq[i+1] = seq[i+1], seq[i]
  return seq

def test_bubble_sort():
  seq = [4,5,3,23,42,6]
  assert(bubble_sort(seq) == sorted(seq))
  print("ㅇㅋ")

test_bubble_sort()