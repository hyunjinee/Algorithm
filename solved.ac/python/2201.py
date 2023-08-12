from bisect import bisect as bs
K = int(input())

dp = [1, 2]
# dp[i] = 2의 거듭 제곱이 되는 i번째 수가 몇번 째에 나오는가

ans = 0
# 출력 할 2진수 형태의 값

while dp[-1]+dp[-2] <= K:
    dp.append(dp[-1]+dp[-2])
# K보다 작은 2의 거듭 제곱 꼴을 모두 찾는다.


while K:
    i = bs(dp, K)-1
    # K가 DP의 몇번째 원소에 들어갈 수 있을 지 찾아서 i에 저장

    ans += 10**i
    # K 보다 작은 가장 큰 2의 거듭제곱을 만드는데 걸리는 횟수를 K에서 제거한다
    # 1 << i == 10**n
    K -= dp[i]

print(ans)


# # import sys
# # input = sys.stdin.readline

# # k = int(input())
# # if k == 1: print(1)
# # else:
# #   fibo = [1, 1]
# #   while fibo[-1] < 1000000000000000000:
# #     fibo.append(fibo[-1] + fibo[-2])
  
# #   result = ''
# #   cnt = 0
# #   for i in fibo:
# #     k -= i 
# #     cnt += 1
# #     if k <= 0:
# #       k += i
# #       break
# #   while cnt :
# #     if fibo[cnt] <= k:
# #       result += '1'
# #       k -= fibo[cnt]
# #     else:
# #       result += '0'
# #     cnt -= 1
# #   print(result)
# # else:
# #     fibo=[1]*101
# #     fibo[1]=2
# #     for i in range(2,101):
# #         fibo[i]=fibo[i-1]+fibo[i-2]
# #     cnt=-1
# #     result='10'
# #     for i in fibo:
# #         k-=i
# #         cnt+=1
# #         if k<=0:
# #             k+=i
# #             break
# #     while True:
# #         if cnt==0: break
# #         if cnt==1:
# #             result+=str(k-1)
# #             break
# #         if k<=fibo[cnt-1]:
# #             result+='0'
# #             cnt-=1
# #         else:
# #             k-=fibo[cnt-1]
# #             cnt-=2
# #             result+='10'
# #     print(result)
            
# import sys

# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())
# dp = [1,1]


# while dp[-1] <= 1000000000000000:
#   dp.append(dp[-2] + dp[-1])

# def find(x):
#   result = ''
#   count = 0
#   while dp[count ] <= x:
#     count += 1
#   count -= 1
#   while count > 0:
#     if dp[count] <= x:
#       result += '1'
#       x -= dp[count]
#     else: 
#       result += '0'
#     count -= 1

#   return result

# print(find(n))
# # # print(find(n))
# #   # while count > 0:
# #   #   if dp[count ] <= x:
# #   #     result += '1'

import sys


fibs = [0, 1]


def main():
    while len(fibs) < 100:
        fibs.append(fibs[-2] + fibs[-1])
    k = int(sys.stdin.readline())
    ans = ["0" for _ in range(100)]
    while k:
        partial_sum = 0
        idx = 1
        while partial_sum + fibs[idx] < k:
            partial_sum += fibs[idx]
            idx += 1
        ans[-idx] = "1"
        print(partial_sum, "qq")
        k -= partial_sum + 1
    print("".join(ans).lstrip("0"))


main()
