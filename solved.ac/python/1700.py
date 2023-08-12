import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
used_order = list(map(int, input().split()))
ans = 0
multitap = []

for idx, used_object in enumerate( used_order ):
  if used_object in multitap:
    continue

  if len(multitap) < n:
    multitap.append(used_object)
    continue

  far_one = 0
  temp = 0

  for mt in multitap:
    if mt not in used_order[idx:]:
      temp = mt
      break
    elif used_order[idx:].index(mt) > far_one:
      far_one = used_order[idx:].index(mt)
      temp = mt
  multitap[multitap.index(temp)] = used_order[idx]
  ans += 1

print(ans)



