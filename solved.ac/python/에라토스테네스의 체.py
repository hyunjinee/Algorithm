"""
하나의 수에 대해서 소수인지 아닌지 판별하는 방법
하지만 특정한 수의 범위 안에 존재하는 모든 소수를 찾을 때는 어떻게 해야할까?
에라토스 테네스의 체 알고리즘을 사용합니다. 

- 다수의 자연수에 대해 소수 여부를 판별할 때 사용하는 대표적인 알고리즘입니다.
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용합니다. 

구체적인 동작 과정은 다음과 같습니다. 
1. 2부터 N까지의 모든 자연수를 나열 합니다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은수 i를 찾습니다. 
3. 남은 수 중에서 i의 배수를 모두 제거합니다. (i는 제거하지 않습니다.)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다. 

예를 들어서 N = 26 이라 하자.
2,3,4,5,6,7,8,9....26 이 있고 2를 제외한 2의 배수는 모두 삭제
3을 제외한 모든 3의 배수는 모두 삭제. 아직 처리하지 않은 가장 작은 수 5를 제외한 5의 배수는 모두 제거
대칭인 수를 활용하면 5까만 확인하면 됩니다.

"""
import math
n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1) :
  if array[i] == True:
    j =  2
    while i * j <= n: 
      array[i* j] = False
      j+=1
    
for i in range(2, n+1):
  if array[i]:
    print(i , end = ' ')