# 기본적 알고리즘

def is_prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True


# 2부터 x-1까지의 대해서 모두 확인해야하므로 시간복잡도는 O(X)

# 약수의 성질
# 모든 약수가 가운데 약수를 기준으로 곱센 연산에 대해 대칭 구조
# 따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됩니다.
# 예를 들어 16이 2로 나누어 떨어진다는것은 8로도 나누어 떨어진다는 것을 의미합니다. 

import math
def is_prime_number2(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False

  return True

