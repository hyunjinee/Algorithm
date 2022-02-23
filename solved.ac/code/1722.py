# k가 주어지면 k번째 순열을 구하고 임의의 순열이 주어지면 이 순열이 몇번째 순열인지 출력

n = int(input())
l = list(map(int, input().split()))
nums = [i for i in range(1, n + 1)]



if l[0] == 1 : 
  k = l[1]
  # k번째 순열을 구한다.
  

