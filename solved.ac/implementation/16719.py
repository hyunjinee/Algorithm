import sys; input = sys.stdin.readline

s = list(input().rstrip())
result = [''] * len(s)

def func(arr,start):
  if not arr:
    return 

  _min = min(arr)
  idx = arr.index(_min)
  result[start+idx] = _min


  print("".join(result))

  func(arr[idx+1:], start+ idx + 1)
  func(arr[:idx], start)

func(s, 0)