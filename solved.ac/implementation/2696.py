import sys, heapq
input = sys.stdin.readline

def solution(data):
  min_q = []
  max_q = []
  mid = data[0]
  result = [mid]

  for idx, val in enumerate(data[1: ]):
    if val > mid:
      heapq.heappush(min_q, val)
    else:
      heapq.heappush(max_q, (-val, val))
    
    if idx % 2 == 1:
      if len(max_q) < len(min_q):
        heapq.heappush(max_q, (-mid, mid))
        mid = heapq.heappop(min_q)
      elif len(max_q) > len(min_q):
        heapq.heappush(min_q, mid)
        mid = heapq.heappop(max_q)[1]
      result.append(mid)
  print(len(result))

  for i in range(len(result)):
    if i != 0 and (i + 1) % 10 == 1:
      print()
    print(result[i], end = ' ')
  print()

for _ in range(int(input())):
  m = int(input()) # 수열의 크기
  data = []

  if m % 10 == 0:
    for _ in range(m//10):
      data.extend(list(map(int,input().split())))
  else:
    for _ in range(m//10 + 1):
      data.extend(list(map(int, input().split())))

  solution(data)
# 100000000

# 길이가 n배열 정렬 nlogn
# 홀수번마다 매번 정렬 -> n^2logn 
# n이 10000이니까 한개의 케이스에 대하여
# 10^8log10^4

# 1초 (최대 가능 연산횟수 = 10 ^ 8) 안에는 해결 할 수 없다.
# 우선 순위큐를 사용한다. 
# 현재 중앙값만 필요하고, 중앙 값보다 큰 값들을 모은 큐와 중앙 값보다 작은 값들을 모은 큐를 둔다.
# 파이썬에서는 heap기능을 위해 heapq라는 라이브러리를 제공한다. 
# 이 라이브러리외에도 PriorityQueue를 사용할 수 있지만, 코딩 테스트 환경에서는 heapq가 더 빠르게 동작하기 때문에 heapq를 사용하는 것이 좋다.
# 파이썬의 힙은 최소힙(부모 노드가 자식 노드보다 크기가 작음)으로 구성되어있다. 
# 그리고 힙은 이진 트리로 만들어져 있어, 삽입 삭제를 하는데 시간복잡도 O(nlogn)에 정렬이 완료된다.


# https://ahntoday.tistory.com/176